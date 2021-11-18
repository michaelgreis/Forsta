import sys
sys.path.append('../')
from classes import ingester as ing

source_bucket = 'snowflaketesting-michael'
target_bucket = 'forsta-processing-6.24.2021'

t_ing = ing.ingester()
t_ing.copy_bucket(source_bucket,target_bucket)
print('Test complete!')