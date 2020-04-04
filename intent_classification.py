from monkeylearn import MonkeyLearn

def classify_intent(msg_body):
    ml = MonkeyLearn('673dabe257b841679b142da12a8cf7683633e7a8')
    data = [msg_body]
    model_id = 'cl_VGoxtFhL'
    result = ml.classifiers.classify(model_id, data)
    # print(result.body)

    classification_result = result.body[0]['classifications']
    confidence = classification_result[0]['confidence']
    intent = classification_result[0]['tag_name']
    # print("Customer query: ", query)
    # print("Intent: ", classification_result[0]['tag_name'])
    return {'confidence':confidence, 'intent':intent}