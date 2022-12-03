import pyezspark
training_public_key = ''
training_private_key = ''
ez = pyezspark.EzSpark(training_public_key, training_private_key = training_private_key, max_number_of_genomes_per_client = 80, max_number_of_trainers = 20)
ez.execute()
