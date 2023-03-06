from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from subdags.subdag_downloads import subdag_downloads
from subdags.subdag_transform import subdag_transform
from groups.group_downloads import download_tasks
from groups.group_transforms import transform_tasks
from datetime import datetime
 
with DAG('group_dag', start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False) as dag:
    
    args = {
        'start_date': dag.start_date,
        'schedule_interval': dag.schedule_interval, 
        'catchup': dag.catchup
    }
    
    # (Opt 1)Running with no subdags/taskgroups
    #This are replaced by the subdag we just freated
    # download_a = BashOperator(
    #     task_id='download_a',
    #     bash_command='sleep 10'
    # )
 
    # download_b = BashOperator(
    #     task_id='download_b',
    #     bash_command='sleep 10'
    # )
 
    # download_c = BashOperator(
    #     task_id='download_c',
    #     bash_command='sleep 10'
    # )
    
    # (Opt 2) Running by subdags
    # downloads = SubDagOperator(
    #     task_id = 'downloads',
    #     subdag = subdag_downloads(
    #         parent_dag_id=dag.dag_id,
    #         child_dag_id='downloads',  #It is important for this to be same as the task_id
    #         args=args
    #     )
    # )
    
    # (Opt 3) Running by task groups
    downloads = download_tasks()
 
 
    ### 
    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )
    ###
          
    # (Opt 1)Running with no subdags/taskgroups
    # transform_a = BashOperator(
    #     task_id='transform_a',
    #     bash_command='sleep 10'
    # )
 
    # transform_b = BashOperator(
    #     task_id='transform_b',
    #     bash_command='sleep 10'
    # )
 
    # transform_c = BashOperator(
    #     task_id='transform_c',
    #     bash_command='sleep 10'
    # )
    
    # (Opt 2) Running by subdags
    # transforms = SubDagOperator(
    #     task_id = 'transforms',
    #     subdag = subdag_transform(
    #         parent_dag_id=dag.dag_id,
    #         child_dag_id='transforms',
    #         args=args
    #     )
    # )
    
    # (Opt 3) Running by task groups
    transforms = transform_tasks()
    # [download_a, download_b, download_c] >> check_files >> [transform_a, transform_b, transform_c]
    # downloads >> check_files >> [transform_a, transform_b, transform_c]
    downloads >> check_files >> transforms