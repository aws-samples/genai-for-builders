from steps.utils import endpoint_exists
from steps.utils import create_training_job_name

from sagemaker.jumpstart.estimator import JumpStartEstimator

def finetune_llama7b(model_id, model_version, endpoint_name, instance_type, num_instances, epoch, max_input_length, instruction_tuned, chat_dataset, train_data_path):

    if endpoint_exists(endpoint_name):
        print("Endpoint already exists")
        training_job_name = None
    else:
        # validation_data_path = model_fine_tuning_config["validation_data_path"] # Not used
        
        training_job_name = create_training_job_name(model_id)

        estimator = JumpStartEstimator(
            model_id=model_id,
            model_version=model_version,
            instance_count=num_instances,
            instance_type=instance_type,
            environment={"accept_eula": "true"},
            disable_output_compression=False)  # For Llama-2-70b, add instance_type = "ml.g5.48xlarge"

        estimator.set_hyperparameters(instruction_tuned=instruction_tuned,
                                      chat_dataset=chat_dataset,
                                      epoch=epoch,
                                      max_input_length=max_input_length)
        
        # estimator.fit({"training": train_data_path, "validation": validation_data_path}) # if there is a validation dataset
        estimator.fit(inputs={"training": train_data_path}, job_name=training_job_name)

        training_job_name = estimator.latest_training_job.name

    return {"training_job_name": training_job_name}
