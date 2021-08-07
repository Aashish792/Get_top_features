def get_top_features(topFeaturesNumber, possibleFeatures, featureRequests):
    '''
    :param topFeaturesNumber: integer
    :param possibleFeatures: array of strings
    :param featureRequests: array of strings
    :return: Most requested top number of features as long as it is a part of possible features.
    '''
    possibleFeaturesDict = {possibleFeatures[i]: 0 for i in range(0, len(possibleFeatures))}
    for featureRequest in featureRequests:
        featureRequestWordList = featureRequest.lower().split()
        for featureRequestWord in featureRequestWordList:
            for possibleFeature in possibleFeaturesDict:
                if possibleFeature in featureRequestWord:
                    possibleFeaturesDict[possibleFeature] += 1

    topKeys = sorted(possibleFeaturesDict, key=possibleFeaturesDict.get, reverse=True)[:topFeaturesNumber]
    return topKeys

feature = get_top_features(topFeaturesNumber=3,
                 possibleFeatures=["storage", "battery", "hover", "alexa", "waterproof", "solar"],
                 featureRequests=[
                     "I wish my Kindle had even more storage",
                     "I wish the battery life on my Kindle lasted 2 years.",
                     "I read in the bath and would enjoy a waterproof Kindle",
                     "Waterproof and increased battery are my top two",
                     "I want to take my Kindle into the shower. Waterproof please waterproof!",
                     "I wanna make my Kindle hover on my desk", "How about a solar Kindle!"])

print(feature)