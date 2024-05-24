from BOOK_SUMMARY.config.configuration import ConfigurationManager
from BOOK_SUMMARY.components.model_evaluation import ModelEvaluation
from BOOK_SUMMARY.logging import logger




class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()