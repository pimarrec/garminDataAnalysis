from getpass import getpass
import garminconnect

from datetime import *
import numpy as np
import json
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
        clean_running.append(tmp)

    #save to file
    return clean_running


def get_heart_rates(startDate,endDate):
    val= []
    resting = []
    numberDays = endDate - startDate
    numberDays = numberDays.days
    for i in range(numberDays):
        time.sleep(1000)
        date = startDate + timedelta(days=i)
        date = date.isoformat()
        heart_rates = garmin.get_heart_rates(date)
        val.append(heart_rates['heartRateValues'])
        resting.append(heart_rates['restingHeartRate'])
    return np.array(val),np.array(resting)



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

startDate = datetime(2023, 5, 5)
#date.today() - timedelta(days=293)
startDate = startDate.isoformat()

endDate = date.today()
endDate = endDate.isoformat()



running = get_clean_running(startDate,endDate)

with open('running_activities.json', 'w') as f:
    json.dump(running, f)


# get activities
# write a startDate  for '2023-10-01'
startDate = datetime(2023, 10, 1)
#date.today() - timedelta(days=293)
startDate = startDate.isoformat()

endDate = date.today()
endDate = endDate.isoformat()

# print(garmin.get_heart_rates(startDate))

yesterday = date.today() - timedelta(days=1)
yesterday = yesterday.isoformat()

#print(garmin.get_sleep_data(yesterday))

# val,rest = get_heart_rates(startDate,endDate)

# hr = garmin.get_activity_hr_in_timezones(14064621864)
# print(hr)


# details = garmin.get_activity_details(14064621864)
# print(details)


# # clean_running = get_clean_running(startDate,endDate)
# # file_name = "running_activities.json"
# # with open(file_name, 'w') as f:
# #     json.dump(clean_running, f)


# # save numpy
# np.save('heart_rates.npy', val)
# np.save('resting_heart_rates.npy', rest)




