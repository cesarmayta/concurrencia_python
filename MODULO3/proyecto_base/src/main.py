from prefect import flow,task
from tasks.task import(
    task
)

@flow(name='ETL SBS')
def main_flow():
    task()
    
    
if __name__ == '__main__':
    main_flow()