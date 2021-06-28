from classes import ingester as ing

#testing configuration
source_bucket = 'snowflaketesting-michael'
object_key = 'Snow_Log/data_0_0_0.json.gz'
target_bucket = 'forsta-processing-6.24.2021'

#Info gathering on bucket
t_ing = ing.ingester()
t_ing.s3_list_buckets()

#Copy files
output_file = t_ing.copy_object(source_bucket,object_key,target_bucket)
print(output_file)

t_ing.convert_object(target_bucket,output_file)