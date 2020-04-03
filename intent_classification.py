from monkeylearn import MonkeyLearn
import get_email

ml = MonkeyLearn('673dabe257b841679b142da12a8cf7683633e7a8')
data = [get_email.msg_body]
model_id = 'cl_VGoxtFhL'
result = ml.classifiers.classify(model_id, data)
print(result.body)

classification_result = result.body[0]['classifications']
confidence = classification_result[0]['confidence']
# print("Customer query: ", query)
# print("Intent: ", classification_result[0]['tag_name'])

def mailInfo():
    return {'intent': classification_result[0]['tag_name'], 'reciver_address': get_email.message['From'], 'confidence': confidence}