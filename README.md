This update adds a new pdf_qa_system() function that:
Loads a PDF file and extracts its text content
Implements a simple question-answering system using keyword matching
Allows users to ask questions about the PDF content
Returns relevant sentences from the PDF that might answer the question
The main menu has been updated to include the new Q&A system option.
The Q&A system is basic but demonstrates the concept:
It removes common stop words from the question
Searches for sentences containing keywords from the question
Returns up to 3 most relevant sentences
--
This program includes:
A structured menu-driven interface
Four different AI-related functions:
- Simple NLP example (basic text analysis)
- Simple Language Model (using bigrams for next word prediction)
- Simple LLM simulation (pattern-based responses)
- Use Case Example (basic sentiment analysis)
- Modular design for easy addition of new features
- Clear separation of concerns with different functions
- Documentation for each function
- Error handling and user input validation
  
The code is designed to be educational and demonstrates basic concepts without external dependencies. Each function implements a simplified version of AI concepts to help understand the fundamentals.

# Shankar Balakrishnan: https://beeshankar.medium.com/the-beginning-of-ai-revolution-human-evolution-part-3b-business-use-cases-aitaas-9c4729604223
# Example program written with the help of cursor co-pilot
