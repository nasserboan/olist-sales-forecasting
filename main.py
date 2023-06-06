import logging
import traceback
import warnings
import mlflow


def _run(entrypoint, parameters={}, source_version=None, use_cache=True):
    """Launching new run for an entrypoint"""

    print(
        "Launching new run for entrypoint=%s and parameters=%s"
        % (entrypoint, parameters)
    )
    submitted_run = mlflow.run(".", entrypoint, parameters=parameters)
    return submitted_run



def workflow():
    """run the workflow"""
    with mlflow.start_run(run_name="PIPE_TESTE1"):
        mlflow.set_tag("mlflow.runName", "somente_date")
        _run("data")


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    logging.basicConfig(
        level=logging.INFO,
        filename="logs/data.log",
        filemode="w+",
        format="%(name)s - %(levelname)s - %(asctime)s - %(message)s",
    )
    logger = logging.getLogger(__name__)

    try:
        workflow()
    except Exception as e:
        print("Exception occured. Check logs.")
        logger.error(f"Failed to run workflow due to error:\n{e}")
        logger.error(traceback.format_exc())