"""Behave environment configuration file"""

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def before_all(context):
    """Setup before all scenarios run"""
    logger.info("Starting test execution")
    # Initialize context attributes if needed
    if not hasattr(context, 'api_endpoint'):
        context.api_endpoint = None
    if not hasattr(context, 'book_id'):
        context.book_id = None
    if not hasattr(context, 'response'):
        context.response = None
    if not hasattr(context, 'status_code'):
        context.status_code = None


def after_all(context):
    """Cleanup after all scenarios run"""
    logger.info("Test execution completed")


def before_scenario(context, scenario):
    """Setup before each scenario"""
    logger.info(f"Starting scenario: {scenario.name}")
    # Reset context for each scenario
    context.api_endpoint = None
    context.book_id = None
    context.response = None
    context.status_code = None


def after_scenario(context, scenario):
    """Cleanup after each scenario"""
    if scenario.status == "failed":
        logger.error(f"Scenario failed: {scenario.name}")
    else:
        logger.info(f"Scenario passed: {scenario.name}")

