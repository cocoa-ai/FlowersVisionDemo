import coremltools

coreml_model = coremltools.converters.caffe.convert(('oxford102.caffemodel', 'deploy.prototxt'), image_input_names = 'data', class_labels = 'flowers.txt')
coreml_model.author = 'Jimmie Goode'
coreml_model.license = 'Unknown'
coreml_model.short_description = 'Classifying images in the Oxford 102 flower dataset with CNNs'
coreml_model.input_description['data'] = 'An image of a flower.'
coreml_model.output_description['prob'] = 'The probabilities for each flower type, for the given input.'
coreml_model.output_description['classLabel'] = 'The most likely type of flower, for the given input.'
coreml_model.save('Oxford102.mlmodel')
