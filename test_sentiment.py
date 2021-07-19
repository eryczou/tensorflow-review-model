import tensorflow as tf

def test_comment(model, sentence):
    print(model.predict([sentence]))

model = tf.keras.models.load_model('amazon_review/1626663669')

test_comment(model, "easy to use and very handy")
