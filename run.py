import os
import json
import openai
from agent import AnalysisAgent
from notebook_generator import generate_notebook


# Initialize the agent
os.environ["VOL_API_KEY"] = "ffd3556a-e883-4581-904e-b96f28bfa919"

agent = AnalysisAgent(
    h5ad_path="/data/luyit/script/git/LabAcceleration/data_match/data/ad4aac9c-28e6-4a1f-ab48-c4ae7154c0cb.h5ad",
    paper_summary_path="/data/luyit/script/git/LabAcceleration/data_match/summary.md",
    openai_api_key=os.environ["VOL_API_KEY"],
    model_name="ep-20250213175001-hd66r",
    analysis_name="Treg",
    num_analyses=3,
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",  # Uncomment and set to your API base URL
    kernel_name='rvq' # Set the kernel name for your conda environment
)

# Run the analysis
agent.run()  # This will run all the analyses the agent decides to attempt.

# Generate Jupyter notebook after analysis is complete
generate_notebook(agent.completed_analyses, agent.output_dir)
