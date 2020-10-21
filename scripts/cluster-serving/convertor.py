import tensorflow as tf
import sys
from optparse import OptionParser


# Use following code to transform Keras h5 to TF savedModel

parser = OptionParser()
parser.add_option("--model_path", type=str, dest="model_path",
                  help="The path of model to convert")
(options, args) = parser.parse_args(sys.argv)

model = tf.keras.models.load_model(options.model_path)
tf.saved_model.save(model, options.model_path.split(".")[0] + "_tf_savedModel")
