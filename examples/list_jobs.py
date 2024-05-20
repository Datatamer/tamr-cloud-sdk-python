from tamr_cloud_sdk.tamr_sdk import TamrApiClient
import time

start = time.time()
tamr_client = TamrApiClient('<host-name>', [('x-api-key', '<api-key>')], grpc_stack_trace=True)
one = time.time()


jobs = tamr_client.jobs()
two = time.time()

response = jobs.list_jobs()
three = time.time()

response = jobs.get_job(job_id='<job-id>')
four = time.time()

print(response)
print(f"APIClient took {one -start}; JobsClient took {two-one} and api call took {three-two} and second is {four-three}")