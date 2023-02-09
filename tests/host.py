import pyezspark
training_public_key = ''
training_private_key = ''
max_number_of_genomes_per_client = 1000
t_val = 1
max_number_of_trainers = 30
threads = 4
ez = pyezspark.EzSpark(training_public_key, training_private_key = training_private_key,
                       max_number_of_genomes_per_client=max_number_of_genomes_per_client,
                       t_val=t_val, max_number_of_trainers=max_number_of_trainers)
ez.execute(threads=threads)
