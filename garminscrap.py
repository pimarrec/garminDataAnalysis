from getpass import getpass
import os
import garminconnect

from datetime import *
import numpy as np
import json
import time as t
import tqdm 


email = "botve.pmarrec@gmail.com"
password = "Pirnoob29"

garmin = garminconnect.Garmin(email, password)
garmin.login()

# print(garmin.display_name)


# ['activityId',
#  'activityName',
#  'description',
#  'startTimeLocal',
#  'startTimeGMT',
#  'activityType',
#  'eventType',
#  'comments',
#  'parentId',
#  'distance',
#  'duration',
#  'elapsedDuration',
#  'movingDuration',
#  'elevationGain',
#  'elevationLoss',
#  'averageSpeed',
#  'maxSpeed',
#  'startLatitude',
#  'startLongitude',
#  'hasPolyline',
#  'ownerId',
#  'ownerDisplayName',
#  'ownerFullName',
#  'ownerProfileImageUrlSmall',
#  'ownerProfileImageUrlMedium',
#  'ownerProfileImageUrlLarge',
#  'calories',
#  'bmrCalories',
#  'averageHR',
#  'maxHR',
#  'averageRunningCadenceInStepsPerMinute',
#  'maxRunningCadenceInStepsPerMinute',
#  'maxLapAvgRunCadence',
#  'averageBikingCadenceInRevPerMinute',
#  'maxBikingCadenceInRevPerMinute',
#  'averageSwimCadenceInStrokesPerMinute',
#  'maxSwimCadenceInStrokesPerMinute',
#  'averageSwolf',
#  'activeLengths',
#  'steps',
#  'conversationUuid',
#  'conversationPk',
#  'numberOfActivityLikes',
#  'numberOfActivityComments',
#  'likedByUser',
#  'commentedByUser',
#  'activityLikeDisplayNames',
#  'activityLikeFullNames',
#  'activityLikeProfileImageUrls',
#  'requestorRelationship',
#  'userRoles',
#  'privacy',
#  'userPro',
#  'courseId',
#  'poolLength',
#  'unitOfPoolLength',
#  'hasVideo',
#  'videoUrl',
#  'timeZoneId',
#  'beginTimestamp',
#  'sportTypeId',
#  'avgPower',
#  'maxPower',
#  'aerobicTrainingEffect',
#  'anaerobicTrainingEffect',
#  'strokes',
#  'normPower',
#  'leftBalance',
#  'rightBalance',
#  'avgLeftBalance',
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
#  'lactateThresholdBpm',
#  'lactateThresholdSpeed',
#  'maxFtp',
#  'avgStrokeDistance',
#  'avgStrokeCadence',
#  'maxStrokeCadence',
#  'workoutId',
#  'avgStrokes',
#  'minStrokes',
#  'deviceId',
#  'minTemperature',
#  'maxTemperature',
#  'minElevation',
#  'maxElevation',
#  'avgDoubleCadence',
#  'maxDoubleCadence',
#  'summarizedExerciseSets',
#  'maxDepth',
#  'avgDepth',
#  'surfaceInterval',
#  'startN2',
#  'endN2',
#  'startCns',
#  'endCns',
#  'summarizedDiveInfo',
#  'activityLikeAuthors',
#  'avgVerticalSpeed',
#  'maxVerticalSpeed',
#  'floorsClimbed',
#  'floorsDescended',
#  'manufacturer',
#  'diveNumber',
#  'locationName',
#  'bottomTime',
#  'lapCount',
#  'endLatitude',
#  'endLongitude',
#  'minAirSpeed',
#  'maxAirSpeed',
#  'avgAirSpeed',
#  'avgWindYawAngle',
#  'minCda',
#  'maxCda',
#  'avgCda',
#  'avgWattsPerCda',
#  'flow',
#  'grit',
#  'jumpCount',
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
#  'excludeFromPowerCurveReports',
#  'totalSets',
#  'activeSets',
#  'totalReps',
#  'minRespirationRate',
#  'maxRespirationRate',
#  'avgRespirationRate',
#  'trainingEffectLabel',
#  'activityTrainingLoad',
#  'avgFlow',
#  'avgGrit',
#  'minActivityLapDuration',
#  'avgStress',
#  'startStress',
#  'endStress',
#  'differenceStress',
#  'maxStress',
#  'aerobicTrainingEffectMessage',
#  'anaerobicTrainingEffectMessage',
#  'splitSummaries',
#  'hasSplits',
#  'moderateIntensityMinutes',
#  'vigorousIntensityMinutes',
#  'maxBottomTime',
#  'hasSeedFirstbeatProfile',
#  'calendarEventId',
#  'calendarEventUuid',
#  'groupRideUUID',
#  'avgGradeAdjustedSpeed',
#  'avgWheelchairCadence',
#  'maxWheelchairCadence',
#  'avgJumpRopeCadence',
#  'maxJumpRopeCadence',
#  'gameName',
#  'differenceBodyBattery',
#  'gameType',
#  'curatedCourseId',
#  'matchedCuratedCourseId',
#  'parent',
#  'favorite',
#  'decoDive',
#  'pr',
#  'purposeful',
#  'manualActivity',
#  'autoCalcCalories',
#  'elevationCorrected',
#  'atpActivity']

# yesterday = date.today() - timedelta(days=1)
# yesterday = yesterday.isoformat()

# print(garmin.get_stats(yesterday))

# # print(garmin.get_user_summary(yesterday))

# print(garmin.get_heart_rates(yesterday))

# print(garmin.get_sleep_data(yesterday))




def get_clean_running(startTime,endTime):
    activities = garmin.get_activities_by_date(startTime, endTime)
    #running =[i for i in activities if i['activityType']['typeId'] == 1]
    #removing none item from each running activities
    clean_running = []
    for i in activities:
        tmp = {}
        for key in i:
            if i['activityType']['typeId'] != 1:
                continue
            if i[key] is str:
                if i[key] != None or i[key][-4:] != ".png":
                    tmp[key] = i[key]
            elif i[key] != None:
                tmp[key] = i[key]
        if tmp != {}:
            clean_running.append(tmp)

    #save to file
    return clean_running


def get_heart_rates(startDate,endDate,val_file = "HR/heart_rates",rest_file = "HR/resting_heart_rates.npy"):
    numberDays = endDate - startDate
    numberDays = numberDays.days
    for i in tqdm.tqdm(range(numberDays)):
        print("Day: ",i)
        
        if os.path.exists(rest_file):
            #val = np.load(val_file,allow_pickle=True)
            rest = np.load(rest_file,allow_pickle=True)
        else:
            #val = np.array([],dtype=int)
            rest = np.array([],dtype=int)
        date = startDate + timedelta(days=i)
        date = date.isoformat()
        heart_rates = garmin.get_heart_rates(date) 
        if heart_rates is not None:
            new_heart_rates = np.array(heart_rates['heartRateValues'])
            #val=np.concatenate((val,new_heart_rates))
            
            rest = np.concatenate((rest,np.array(heart_rates['restingHeartRate']).reshape(1)))
        else :
            print("No heart rate data for day: ",date)
        np.save(val_file+"{}.npy".format(date), new_heart_rates)
        np.save(rest_file, rest)
        t.sleep(600)
    # return val,rest




def get_sleep_data(startDate,endDate):
    val= []
    numberDays = endDate - startDate
    numberDays = numberDays.days
    for i in range(numberDays):
        tmp= []
        d = startDate + timedelta(days=i)
        d = d.isoformat()
        sleep = garmin.get_sleep_data(d)
        val.append(sleep['sleepData'])
    return np.array(val)



def get_activities_details(activities : list):
    for activity in tqdm.tqdm(activities):
        #print(activity.keys())
        if activity == {}:
            continue
        activity_id = activity['activityId']
        liste = os.listdir('details')
        if str(activity_id)+".json" in liste:
            continue
        print("Activity: ",activity["activityId"])
        try:
            activity_details = garmin.get_activity_details(activity_id, maxchart=4000, maxpoly=8000)
        except garminconnect.GarminConnectTooManyRequestsError:
            print("Too many requests, waiting 5 minutes")
            t.sleep(300)
            activity_details = garmin.get_activity_details(activity_id, maxchart=4000, maxpoly=8000)
        except garminconnect.GarminConnectConnectionError:
            print("Connection Error, waiting 5 minutes")
            t.sleep(300)
            activity_details = garmin.get_activity_details(activity_id, maxchart=4000, maxpoly=8000)
        except garminconnect.GarminConnectAuthenticationError:
            print("Authentication Error, waiting 5 minutes")
            break
        except Exception as e:
            print("Unknown error: ", e)
        
        with open('details/{}.json'.format(activity_id), 'w') as f:
            json.dump(activity_details, f)
        #t.sleep(100)
    return activities



# get activities
# write a startDate  for '2023-10-01'
startDate = datetime(2023, 5, 6)
#date.today() - timedelta(days=293)
# startDate = startDate.isoformat()

endDate = datetime.today()
# endDate = endDate.isoformat()

#get_heart_rates(startDate,endDate)

# yesterday = date.today() - timedelta(days=1)
# yesterday = yesterday.isoformat()

# print(garmin.get_sleep_data(yesterday))

# val,rest = get_heart_rates(startDate,endDate)


clean_running = get_clean_running(startDate,endDate)
file_name = "running_activities.json"
with open(file_name, 'w') as f:
    json.dump(clean_running, f)


# # save numpy
# np.save('heart_rates.npy', val)
# np.save('resting_heart_rates.npy', rest)

with open('running_activities.json', 'r') as f:
    clean_running = json.load(f)

get_activities_details(clean_running)


# activity_details = garmin.get_activity_details(14124525955,maxchart=4000,maxpoly=8000)
# print(activity_details)

#  'activityId',
#  'activityName',
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