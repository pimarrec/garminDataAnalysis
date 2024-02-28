import json
import os
import numpy as np
import datetime
import matplotlib.pyplot as plt
# hr = garmin.get_activity_hr_in_timezones(14064621864)
# print(hr)


# details = garmin.get_activity_details(14064621864)
# print(details)


#TODO get the details and get the HR for the interval
#TODO do some analysis on the HR (maybe with the time zones) 
#     maybe also with a histogram of the HR for each rate

#  'activityId',
#  'activityName',
#   "startTimeLocal"
#  'description',
#  'distance',
#  'duration',
#  'activityType',
#  'elapsedDuration',
#  'movingDuration',
#  'elevationGain',
#  'elevationLoss',
#  'averageSpeed',
#  'maxSpeed',
#  'startTimeLocal',
#  'startTimeGMT',
#  'averageHR',
#  'maxHR',
#  'averageRunningCadenceInStepsPerMinute',
#  'maxRunningCadenceInStepsPerMinute',
#  'steps',
#  'max20MinPower',
#  'avgVerticalOscillation',
#  'avgGroundContactTime',
#  'avgStrideLength',
#  'avgFractionalCadence',
#  'maxFractionalCadence',
#  'trainingStressScore',
#  'intensityFactor',
#  'vO2MaxValue',
#  'avgVerticalRatio',
#  'avgGroundContactBalance',
#  'minTemperature',
#  'maxTemperature',
#  'minElevation',
#  'maxElevation',
#  'avgDoubleCadence',
#  'maxDoubleCadence',
#  'avgVerticalSpeed',
#  'maxVerticalSpeed',
#  'floorsClimbed',
#  'floorsDescended',
#  'caloriesEstimated',
#  'caloriesConsumed',
#  'waterEstimated',
#  'waterConsumed',
#  'maxAvgPower_1',
#  'maxAvgPower_2',
#  'maxAvgPower_5',
#  'maxAvgPower_10',
#  'maxAvgPower_20',
#  'maxAvgPower_30',
#  'maxAvgPower_60',
#  'maxAvgPower_120',
#  'maxAvgPower_300',
#  'maxAvgPower_600',
#  'maxAvgPower_1200',
#  'maxAvgPower_1800',
#  'maxAvgPower_3600',
#  'maxAvgPower_7200',
#  'maxAvgPower_18000',
#  'splitSummaries',
#  'hasSplits',

file_name = "running_activities.json"
with open(file_name, 'r') as f:
    # load the json file
    act = json.load(f)
    

save_folder = "marathon_prep"

# reverse act
act = act[::-1]

dates = []
distance = []
duration = []
hr_avg = []
cadence_avg = []
max_hr = []

distance_run = []
duration_run = []
hr_avg_run = []
cadence_avg_run = []

distance_spe = []
duration_spe = []
hr_avg_spe = []
cadence_avg_spe = []

# I have to do the analyze of the details data to get the HR of the interval...
startDate = datetime.date(2023,10,25)

for i in act:
    if i == {}:
        continue
    if i['distance'] == 0:
        continue
    # selection at 1 december
    if datetime.date.fromisoformat(i['startTimeLocal'][:10]) < startDate:
        continue
    dates.append(datetime.date.fromisoformat(i['startTimeLocal'][:10]))
    distance.append(i['distance']) # in meters
    duration.append(i['duration']) # in seconds
    hr_avg.append(i['averageHR'])
    max_hr.append(i['maxHR'])
    cadence_avg.append(i['averageRunningCadenceInStepsPerMinute'])

    for j in i['splitSummaries']:
        if j['splitType'] == "RWD_RUN":
            distance_run.append(j['distance'])
            duration_run.append(j['duration'])
        elif j['splitType'] == "INTERVAL_ACTIVE":
            distance_spe.append(j['distance'])
            duration_spe.append(j['duration'])


def get_last_seven_idx(date,dates):
    # date is a unique datetime object
    # dates is a np of datetime object
    # act is a list of dict

    #get the np bool of the last seven days from date
    dates= np.array(dates)
    last_seven_idx = np.zeros(dates.shape[0],dtype=bool)
    for i,d in enumerate(dates):
        if (date - d).days <= 7 and (date - d).days >= 0:
           last_seven_idx[i] = True
    return np.array(last_seven_idx)

# turn everything in np.array
#dates = np.array(dates)
print(len(dates))
distance = np.array(distance)
duration = np.array(duration)
hr_avg = np.array(hr_avg)
cadence_avg = np.array(cadence_avg)
max_hr = np.array(max_hr)

distance_run = np.array(distance_run)
duration_run = np.array(duration_run)

distance_spe = np.array(distance_spe)
duration_spe = np.array(duration_spe)

speed = distance_run/duration_run * 3.6 # in km/h
speed_spe = distance_spe/duration_spe * 3.6 # in km/h


# id = np.argwhere(distance==0)
# print(dates[id[0][0]])
# print(act[id[0][0]])

allure = (1000*duration_run)/(60*distance_run) # in min/km
allure_spe = (1000*duration_spe)/(60*distance_spe) # in min/km

# print all shape in one only print with the label
# print("distance: ",distance.shape)
# print("duration: ",duration.shape)
# print("hr_avg: ",hr_avg.shape)
# print("cadence_avg: ",cadence_avg.shape)

# print("distance_run: ",distance_run.shape)
# print("duration_run: ",duration_run.shape)
# print("distance_spe: ",distance_spe.shape)
# print("duration_spe: ",duration_spe.shape)
# print("speed: ",speed.shape)
# print("speed_spe: ",speed_spe.shape)
# print("allure: ",allure.shape)
# print("allure_spe: ",allure_spe.shape)

max_allure = np.max(allure)
BPM_MAX = max_hr.max()
print(BPM_MAX)

score = (1-(allure*hr_avg)/(max_allure*BPM_MAX))*100

effort = np.power(distance/1000,3*(hr_avg/BPM_MAX))

shr = duration*hr_avg/(3600*BPM_MAX)


cum_7_distance = []
cum_7_duration = []

cum_7_score = []
cum_7_effort = []
cum_7_shr = []
mean_7_hr = []
mean_7_cadence = []


for i in dates:
    last_seven_idx = get_last_seven_idx(i,dates)
    cum_7_distance.append(np.sum(distance[last_seven_idx])/1000)
    cum_7_duration.append(np.sum(duration[last_seven_idx])/3600)
    cum_7_score.append(np.mean(score[last_seven_idx]))
    cum_7_effort.append(np.sum(effort[last_seven_idx]))  
    cum_7_shr.append(np.sum(shr[last_seven_idx]))  
    mean_7_hr.append(np.mean(hr_avg[last_seven_idx]))
    mean_7_cadence.append(np.mean(cadence_avg[last_seven_idx]))



cum_7_distance = np.array(cum_7_distance)
cum_7_duration = np.array(cum_7_duration)
cum_7_score = np.array(cum_7_score)
cum_7_effort = np.array(cum_7_effort)
cum_7_shr = np.array(cum_7_shr)
mean_7_hr = np.array(mean_7_hr)
mean_7_cadence = np.array(mean_7_cadence)

# abssice is the date from the beginning of the first dates to the last one

# print 4 graph 
# high definition

# fig, axs = plt.subplots(3, 2)
# fig.suptitle('Running activities')
# axs[0, 0].bar(dates, distance/1000, color = 'tab:blue')
# axs[0, 0].set_title('distance')
# axs[0, 1].bar(dates, duration/3600, color = 'tab:orange')
# axs[0, 1].set_title('duration')
# axs[1, 0].plot(dates, hr_avg, color = 'tab:green')
# axs[1, 0].set_title('hr_avg')
# axs[1, 1].plot(dates, cadence_avg, color = 'tab:red')
# axs[1, 1].set_title('cadence_avg')
# axs[2, 0].plot(dates, score, color = 'tab:purple')
# axs[2, 0].set_title('score')
# axs[2, 1].plot(dates, effort, color = 'tab:brown')
# axs[2, 1].set_title('effort')

# # high definition for the image
# plt.savefig("running_activities.png",dpi=1000)
# plt.close()

# print 4 graph cum 7
# fig, axs = plt.subplots(2, 2)
# fig.suptitle('Running activities')
# axs[0, 0].plot(dates, cum_7_distance, color = 'tab:blue')
# axs[0, 0].set_title('cum_7_distance')
# axs[0, 1].plot(dates, cum_7_duration, color = 'tab:orange')
# axs[0, 1].set_title('cum_7_duration')
# axs[1, 0].plot(dates, cum_7_score, color = 'tab:green')
# axs[1, 0].set_title('cum_7_score')
# axs[1, 1].plot(dates, cum_7_effort, color = 'tab:red')
# axs[1, 1].set_title('cum_7_effort')

# plt.savefig("running_activities_cum_7.png",dpi=1000)
# plt.close()

def plot_all():
    ## print each graph one by one, save and them close
    # distance
    plt.bar(dates, distance/1000, color = 'tab:blue')
    plt.title('distance')
    plt.savefig(os.path.join(save_folder,"distance.png"),dpi=500)
    plt.close()

    # duration
    plt.bar(dates, duration/3600, color = 'tab:orange')
    plt.title('duration')
    plt.savefig(os.path.join(save_folder,"duration.png"),dpi=500)
    plt.close()

    # hr_avg
    plt.plot(dates, hr_avg, color = 'tab:green')
    plt.title('hr_avg')
    plt.savefig(os.path.join(save_folder,"hr_avg.png"),dpi=500)
    plt.close()

    # cadence_avg
    plt.plot(dates, cadence_avg, color = 'tab:red')
    plt.title('cadence_avg')
    plt.savefig(os.path.join(save_folder,"cadence_avg.png"),dpi=500)
    plt.close()

    # score
    plt.plot(dates, score, color = 'tab:purple')
    plt.title('score')
    plt.savefig(os.path.join(save_folder,"score.png"),dpi=500)
    plt.close()

    # effort
    plt.plot(dates, effort, color = 'tab:brown')
    plt.title('effort')
    plt.savefig(os.path.join(save_folder,"effort.png"),dpi=500)
    plt.close()

    # allure
    plt.plot(dates, allure, color = 'tab:pink')
    plt.title('allure')
    plt.savefig(os.path.join(save_folder,"allure.png"),dpi=500)
    plt.close()

    # cum_7_distance
    plt.plot(dates, cum_7_distance, color = 'tab:blue')
    plt.title('cum_7_distance')
    plt.savefig(os.path.join(save_folder,"cum_7_distance.png"),dpi=500)
    plt.close()

    # cum_7_duration
    plt.plot(dates, cum_7_duration, color = 'tab:orange')
    plt.title('cum_7_duration')
    plt.savefig(os.path.join(save_folder,"cum_7_duration.png"),dpi=500)
    plt.close()

    # cum_7_score
    plt.plot(dates, cum_7_score, color = 'tab:green')
    plt.title('cum_7_score')
    plt.savefig(os.path.join(save_folder,"mean_7_score.png"),dpi=500)
    plt.close()

    # cum_7_effort
    plt.plot(dates, cum_7_effort, color = 'tab:red')
    plt.title('cum_7_effort')
    plt.savefig(os.path.join(save_folder,"cum_7_effort.png"),dpi=500)
    plt.close()

    # shr
    plt.plot(dates, shr, color = 'tab:purple')
    plt.title('shr')
    plt.savefig(os.path.join(save_folder,"shr.png"),dpi=500)    
    plt.close()

    # cum_7_shr
    plt.plot(dates, cum_7_shr, color = 'tab:brown')
    plt.title('cum_7_shr')
    plt.savefig("cum_7_shr.png",dpi=500)
    plt.close()

    # mean_7_hr
    plt.plot(dates, mean_7_hr, color = 'tab:orange')
    plt.title('mean_7_hr')
    plt.savefig(os.path.join(save_folder,"mean_7_hr.png"),dpi=500)
    plt.close()

    # mean_7_cadence
    plt.plot(dates, mean_7_cadence, color = 'tab:purple')
    plt.title('mean_7_cadence')
    plt.savefig(os.path.join(save_folder,"mean_7_cadence.png"),dpi=500)
    plt.close()

plot_all()


def mean_std(arr):
    return np.mean(arr),np.std(arr)

def print_mean_std(arr):
    print("mean: ",np.mean(arr))
    print("std: ",np.std(arr))

def mean_curve(arr,window=7):
    ## not really good because the point are not eqaully spaced
    mean = np.zeros(arr.shape[0]-window+1)
    for i in range(arr.shape[0]-window+1):
        mean[i] = np.mean(arr[i:i+window])
    return mean

# dates_cut = dates[:-6]
# mean_curve_hr_avg = mean_curve(hr_avg,7)
# mean_curve_cadence_avg = mean_curve(cadence_avg,7)
# mean_curve_score = mean_curve(score,7)
# mean_curve_effort = mean_curve(effort,7)
# mean_curve_shr = mean_curve(shr,7)


# plt.plot(dates_cut,mean_curve_hr_avg, color = 'tab:green')
# plt.title('mean_curve_hr_avg')
# plt.savefig(os.path.join(save_folder,"mean_curve_hr_avg.png"),dpi=500)
# plt.close()

# plt.plot(dates_cut,mean_curve_cadence_avg, color = 'tab:red')
# plt.title('mean_curve_cadence_avg')
# plt.savefig(os.path.join(save_folder,"mean_curve_cadence_avg.png"),dpi=500)
# plt.close()

# plt.plot(dates_cut,mean_curve_score, color = 'tab:purple')
# plt.title('mean_curve_score')
# plt.savefig(os.path.join(save_folder,"mean_curve_score.png"),dpi=500)
# plt.close()


# plt.plot(dates_cut,mean_curve_effort, color = 'tab:brown')
# plt.title('mean_curve_effort')
# plt.savefig(os.path.join(save_folder,"mean_curve_effort.png"),dpi=500)
# plt.close()


# plt.plot(dates_cut,mean_curve_shr, color = 'tab:orange')
# plt.title('mean_curve_shr')
# plt.savefig(os.path.join(save_folder,"mean_curve_shr.png"),dpi=500)
# plt.close()


def save_csv(file_name):
    # save all the data in a csv file
    import csv
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["date","distance","duration","hr_avg","cadence_avg","max_hr","distance_run","duration_run","distance_spe","duration_spe","speed","speed_spe","allure","allure_spe","score","effort","shr","cum_7_distance","cum_7_duration","cum_7_score","cum_7_effort","cum_7_shr","mean_7_hr","mean_7_cadence"])
        for i in range(len(dates)):
            writer.writerow([dates[i],distance[i]/1000,duration[i]/3600,hr_avg[i],cadence_avg[i],max_hr[i],distance_run[i]/1000,duration_run[i]/3600,distance_spe[i]/1000,duration_spe[i]/3600,speed[i],speed_spe[i],allure[i],allure_spe[i],score[i],effort[i],shr[i],cum_7_distance[i],cum_7_duration[i],cum_7_score[i],cum_7_effort[i],cum_7_shr[i],mean_7_hr[i],mean_7_cadence[i]])

save_csv(os.path.join(save_folder,"running_activities.csv"))








