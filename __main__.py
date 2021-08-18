import pulumi
import pulumi_gcp as gcp
import os
import pulumi.automation as auto



def create_sa(name: str):
    return gcp.serviceaccount.Account(
        name,
        account_id=name + "-service-account",
        display_name=name + "-service-account")


def pulumi_program():
    create_sa("team1")


stack = pulumi.automation.create_or_select_stack(
    stack_name="dev",
    project_name="intrepid-memory-321513",
    program=pulumi_program())

# team_path = os.getcwd() + '/teams'
# team_list = [f for f in os.listdir(team_path) if os.path.isdir(os.path.join(team_path, f))]
    
# def create_sa(name: str):
#     return gcp.serviceaccount.Account(
#         name,
#         account_id=name + "-service-account",
#         display_name=name + "-service-account")


# def create_layer(team: str):
#     return create_sa(team)





# try:
#     stack = pulumi.automation.create_or_select_stack(
#         stack_name="dev",
#         project_name="intrepid-memory-321513",
#         program=pulumi_program())
#     stack.set_config("gcp:region", auto.ConfigValue("northamerica-northeast1"))
#     stack.set_config("gcp:project", auto.ConfigValue("intrepid-memory-321513"))
#     stack.up(on_output=print)
# except auto.StackAlreadyExistsError:
#     print(f"Error: ***")
