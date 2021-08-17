import pulumi
import os
from pulumi_gcp import storage, serviceaccount



def create_sa(name):
    sa = serviceaccount.Account(
        name,
        account_id=name + "-service-account",
        display_name=name + "-service-account")


def pulumi_program():
    print('CURRENT WORKING: ' + os.getcwd())
    team_path = '/workspace/teams/'
    team_list = [f for f in os.listdir(team_path) if os.path.isdir(os.path.join(team_path, f))]
    for team in team_list:
        create_sa(team)


stack = pulumi.automation.create_or_select_stack(
    stack_name="team1",
    project_name="intrepid-memory-321513",
    program=pulumi_program)


ws = stack.workspace()
ws.install_plugin("gcp", "v5.15.0")

preview = stack.preview()
print(preview)

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_mode', '_run_pulumi_cmd_sync', 'cancel', 'create', 'create_or_select', 'destroy', 'export_stack', 'get_all_config', 'get_config', 'history', 'import_stack', 'info', 'name', 'outputs', 'preview', 'refresh', 'refresh_config', 'remove_all_config', 'remove_config', 'select', 'set_all_config', 'set_config', 'up', 'workspace']



# from pulumi import resource
# import yaml
# import pulumi
# import pprint
# import sys
# import os
# from pulumi_gcp import storage, bigquery, serviceaccount
# from cerberus import Validator

# # sys.tracebacklimit = None

# def dataset(manifest: str) -> None:
#     bigquery.Dataset(
#         resource_name=manifest['resource_name'],
#         dataset_id=manifest['dataset_id'],
#         description=manifest['description'],
#         labels={'cost_center': manifest['metadata']['cost_center'], 'dep': manifest['metadata']['dep']},
#         default_partition_expiration_ms=manifest['partition_expiration_ms'],
#         default_table_expiration_ms=manifest['table_expiration_ms'],
#         delete_contents_on_destroy=True,
#         location='northamerica-northeast1'
#     )


# def dataset_user_access(manifest: str, user: str, role: str) -> None:
#     bigquery.DatasetAccess(
#         resource_name=manifest['resource_name'],
#         dataset_id=manifest['dataset_id'],
#         user_by_email=user,
#         role=role
#     )


# def table(manifest: str) -> None:
#     return bigquery.Table(
#         resource_name=manifest['resource_name'],
#         dataset_id=manifest['dataset_id'],
#         table_id=manifest['table_id'],
#         deletion_protection=False,
#         expiration_time=manifest['expiration_ms'],
#         friendly_name=manifest['friendly_name'],
#         labels={'cost_center': manifest['metadata']['cost_center'], 'dep': manifest['metadata']['dep']},
#         schema=manifest['schema']
#     )


# def query(manifest: str) -> None:
#     return bigquery.DataTransferConfig(
#         resource_name=manifest['resource_name'],
#         display_name=manifest['display_name'],
#         # data_refresh_window_days=manifest['data_refresh_window_days'],
#         data_source_id=manifest['data_source_id'],
#         schedule=manifest['schedule'],
#         destination_dataset_id=manifest['destination_dataset_id'],
#         location='northamerica-northeast1',
#         params={
#             "destination_table_name_template": manifest['params']['destination_table_name'],
#             "write_disposition": manifest['params']['write_disposition'],
#             "query": manifest['params']['query'],
#         },
#         # labels=[{"team": "tsbt"}]
#     )


# def get_dataset(manifest):
#     return bigquery.Dataset.get(
#         resource_name=manifest['resource_name'],
#         id=manifest['dataset_id']
#     )


# def table_user_access(manifest, table_ref) -> None:
#     readers = manifest['access']['readers']
#     readers = ["user:" + reader for reader in readers]
#     bigquery.IamBinding(
#         resource_name=manifest['resource_name'],
#         dataset_id=manifest['dataset_id'],
#         table_id=table_ref.table_id,
#         role='roles/bigquery.dataViewer',
#         members=readers
#     )


# def validate_table_manifest(manifest):
#     schema = eval(open('./schemas/table.py', 'r').read())
#     validator = Validator(schema)
#     if validator.validate(manifest, schema):
#         return
#     else:
#         raise Exception(validator.errors)


# def validate_query_manifest(manifest):
#     schema = eval(open('./schemas/query.py', 'r').read())
#     validator = Validator(schema)
#     if validator.validate(manifest, schema):
#         return
#     else:
#         raise Exception(validator.errors)


# def validate_dataset_manifest(manifest):
#     schema = eval(open('./schemas/dataset.py', 'r').read())
#     validator = Validator(schema)
#     if validator.validate(manifest, schema):
#         return
#     else:
#         raise Exception(validator.errors)


# def update(path: str) -> None:
#     with open(path) as f:
#         manifest = yaml.safe_load(f)
#         if manifest and manifest['type'] == 'dataset':
#             validate_dataset_manifest(manifest)
#             dataset(manifest)
#             # print(get_dataset(manifest))
#         if manifest and manifest['type'] == 'table':
#             validate_table_manifest(manifest)
#             t = table(manifest)
#             table_user_access(manifest, t)
#         if manifest and manifest['type'] == 'query':
#             # validate_query_manifest(manifest)
#             query(manifest)


# # def update_access(path: str) -> None:
# #         manifest = load_manifest(path)
# #         if manifest and manifest['type'] == 'dataset':
# #             # [dataset_user_access(manifest, reader, 'READER') for reader in manifest['readers'] if not None]
# #             for reader in manifest['readers'] or []:
# #                 dataset_user_access(manifest, reader, 'READER')
# #             # for writer in manifest['writer'] or []:
# #             #     dataset_user_access(manifest, writer, 'WRITER')
# #         if manifest and manifest['type'] == 'table':
# #             table_user_access(manifest)



# def load_manifest(path):
#     manifest = open(path + 'manifest.yaml', 'r')
#     try:
#         return yaml.safe_load(manifest)
#     except yaml.YAMLError as exception:
#         raise exception


# def create_sa(name):
#     sa = serviceaccount.Account(
#         name,
#         account_id=name + "-service-account",
#         display_name=name + "-service-account")
#     # serviceaccount.IAMMember(
#     #     resource_name=name + "-data-editor-iam",
#     #     service_account_id=sa.name,
#     #     role="roles/iam.serviceAccountUser",
#     #     member=sa.email.apply(lambda email: f"serviceAccount:{email}"))


# def pulumi_program():
#     print('CURRENT WORKING: ' + os.getcwd())
#     team_path = '/workspace/teams/'
#     team_list = [f for f in os.listdir(team_path) if os.path.isdir(os.path.join(team_path, f))]
#     for team in team_list:
#         create_sa(team)


#     f = open('/workspace/DIFF_LIST.txt')
#     for path in f.read().splitlines():
#         update(path)




# print('CURRENT WORKING: ' + os.getcwd())
# team_path = '/workspace/teams/'
# team_list = [
#     f
#     for f in os.listdir(team_path)
#     if os.path.isdir(os.path.join(team_path, f))
# ]

# manifest_list = [
#     os.path.join(team_path, f)
#     for f in os.listdir(team_path)
# ]


# for team in team_list:
#     create_sa(team)


# for path, subdirs, files in os.walk('/workspace/teams'):
#     for name in files:
#         if name.endswith('manifest.yaml'):
#             update(os.path.join(path, name))



# # f = open('/workspace/DIFF_LIST.txt')
# # for path in f.read().splitlines():
# #     update(path)
