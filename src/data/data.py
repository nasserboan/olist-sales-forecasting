import mlflow
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go():
    logger.info('starting_data_pipeline_component')
    with mlflow.active_run as run:
        mlflow.log_params({'data-pipe-params':1})


if __name__ == "__main__":
    go()