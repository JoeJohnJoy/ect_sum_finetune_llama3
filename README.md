# Fine tuning Llama3 model for earning call transcripts

### Notes
- Most of the code was run on Google Colab for available GPU
- The model fine tuned is a quantised version from Unsloth
- The model was fine tuned using Unsloth since the training speed was better than other libraries
- It can be fine tuned using hugging face libraries too but there will be significant increase the time taken
- the data was prepared in Alpaca format with instruction, input and output with instructions were generated using bigger and more accuratr models.


### Steps to follow

- Following are the steps required to fine tune llama 3 model

1. data_prep notebook helps in preparing the data in alpaca format - ie with instruction, input and output
2. the model is fine-tuned using unsloth and by loading the data using load_dataset from hugging face
3. Once the model is fine tune the models are saved locally as well as pushed to hugging face
4. Models can be quantised to created gguf versions of it using llama.cpp
5. The GGUF version can be pushed to hugging face
6. Inference was done using Unsloth,
7. Fow now the evaluation are human eval since the number of fine-tuning steps were bare 100
8. The model generated in quantised GGUF version can be hosted locally using ollama
9. Instruction to host in Ollama has been mentioned in the Makefile in models folder


###

From the preliminary inspection it looks like with even 100 steps of fine tuning, the model generates responses closer to the format 
of the required output


