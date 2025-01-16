# Shankar Balakrishnan: https://beeshankar.medium.com/the-beginning-of-ai-revolution-human-evolution-part-3b-business-use-cases-aitaas-9c4729604223
# Let's learn AI using Python
# Example program written with the help of cursor co-pilot
# Added additional options to explore LLM with model trained using a local PDF file
def simple_nlp_example():
    """Simple NLP example using basic text processing"""
    print("\n=== Simple NLP Demo ===")
    text = input("Enter a sentence for analysis: ")
    
    # Basic text analysis
    word_count = len(text.split())
    char_count = len(text)
    words = text.lower().split()
    
    # Simple word frequency
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    print(f"\nAnalysis Results:")
    print(f"Word count: {word_count}")
    print(f"Character count: {char_count}")
    print(f"Word frequency: {word_freq}")

def simple_language_model():
    """Simple statistical language model for next word prediction"""
    print("\n=== Simple Language Model Demo ===")
    
    # Training data (could be expanded)
    training_text = """
    the cat sat on the mat
    the dog ran in the park
    the bird flew over the tree
    """
    
    # Create simple bigram model
    words = training_text.lower().split()
    bigrams = {}
    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word not in bigrams:
            bigrams[current_word] = {}
        bigrams[current_word][next_word] = bigrams[current_word].get(next_word, 0) + 1
    
    # Prediction
    while True:
        word = input("\nEnter a word (or 'quit' to exit): ").lower()
        if word == 'quit':
            break
            
        if word in bigrams:
            next_word_predictions = bigrams[word]
            print(f"Possible next words: {list(next_word_predictions.keys())}")
        else:
            print("Word not found in training data")

def simple_llm():
    """Simple rule-based LLM simulation"""
    print("\n=== Simple LLM Demo ===")
    
    # Simple pattern matching responses
    responses = {
        "hello": "Hello! How can I help you today?",
        "how are you": "I'm functioning well, thank you for asking!",
        "what is ai": "AI (Artificial Intelligence) is the simulation of human intelligence by machines.",
        "bye": "Goodbye! Have a great day!"
    }
    
    while True:
        user_input = input("\nEnter your message (or 'quit' to exit): ").lower()
        if user_input == 'quit':
            break
            
        # Simple pattern matching
        response = "I'm not sure how to respond to that."
        for pattern, reply in responses.items():
            if pattern in user_input:
                response = reply
                break
        
        print(f"AI: {response}")

def use_case_example():
    """Demonstration of a simple sentiment analysis use case"""
    print("\n=== Sentiment Analysis Use Case Demo ===")
    
    # Simple sentiment analysis using keyword matching
    positive_words = {'good', 'great', 'excellent', 'amazing', 'wonderful', 'happy'}
    negative_words = {'bad', 'terrible', 'awful', 'horrible', 'sad', 'poor'}
    
    text = input("Enter a review or comment for sentiment analysis: ").lower()
    words = set(text.split())
    
    positive_score = len(words.intersection(positive_words))
    negative_score = len(words.intersection(negative_words))
    
    print("\nSentiment Analysis Results:")
    print(f"Positive words found: {words.intersection(positive_words)}")
    print(f"Negative words found: {words.intersection(negative_words)}")
    
    if positive_score > negative_score:
        print("Overall sentiment: Positive")
    elif negative_score > positive_score:
        print("Overall sentiment: Negative")
    else:
        print("Overall sentiment: Neutral")

def read_pdf_for_training():
    """Read text from PDF files for LLM training"""
    try:
        import PyPDF2
    except ImportError:
        print("\nError: PyPDF2 library not found.")
        print("Please install it using: pip install PyPDF2")
        return

    print("\n=== PDF Reader for LLM Training ===")
    pdf_path = input("Enter the path to your PDF file: ")

    try:
        # Open and read the PDF file
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text_content = ""

            # Extract text from each page
            for page in pdf_reader.pages:
                text_content += page.extract_text()

            # Basic text statistics
            words = text_content.split()
            unique_words = set(words)

            print("\nPDF Analysis Results:")
            print(f"Total pages: {len(pdf_reader.pages)}")
            print(f"Total words: {len(words)}")
            print(f"Unique words: {len(unique_words)}")
            
            # Preview of the content
            preview_length = 200
            print(f"\nContent preview (first {preview_length} characters):")
            print(text_content[:preview_length] + "...")

    except FileNotFoundError:
        print(f"\nError: File '{pdf_path}' not found.")
    except Exception as e:
        print(f"\nError reading PDF: {str(e)}")

def pdf_qa_system():
    """Question-Answering system using PDF content"""
    try:
        import PyPDF2
    except ImportError:
        print("\nError: PyPDF2 library not found.")
        print("Please install it using: pip install PyPDF2")
        return

    print("\n=== PDF-based Q&A System ===")
    pdf_path = input("Enter the path to your PDF file: ")

    try:
        # Load and process PDF content
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text_content = ""
            for page in pdf_reader.pages:
                text_content += page.extract_text()

        print("\nPDF loaded successfully! You can now ask questions about its content.")
        print("(Type 'quit' to exit)")

        while True:
            question = input("\nYour question: ").lower()
            if question == 'quit':
                break

            # Simple keyword-based answer retrieval
            # Split content into sentences (basic implementation)
            sentences = text_content.replace('\n', ' ').split('.')
            relevant_sentences = []

            # Search for sentences containing question keywords
            question_words = set(question.split()) - {'what', 'why', 'how', 'when', 'where', 'who', 'is', 'are', 'the', 'a', 'an'}
            for sentence in sentences:
                sentence = sentence.strip()
                if any(word in sentence.lower() for word in question_words):
                    relevant_sentences.append(sentence)

            if relevant_sentences:
                print("\nRelevant information found:")
                for i, sentence in enumerate(relevant_sentences[:3], 1):
                    print(f"{i}. {sentence}")
            else:
                print("\nSorry, I couldn't find relevant information to answer your question.")

    except FileNotFoundError:
        print(f"\nError: File '{pdf_path}' not found.")
    except Exception as e:
        print(f"\nError processing PDF: {str(e)}")

def main():
    """Main function to handle menu and program flow"""
    while True:
        print("\n=== AI Learning Examples ===")
        print("1. Natural Language Processing Example")
        print("2. Simple Language Model")
        print("3. Simple LLM Demo")
        print("4. Use Case Example (Sentiment Analysis)")
        print("5. Read PDF for Training")
        print("6. PDF Q&A System")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            simple_nlp_example()
        elif choice == '2':
            simple_language_model()
        elif choice == '3':
            simple_llm()
        elif choice == '4':
            use_case_example()
        elif choice == '5':
            read_pdf_for_training()
        elif choice == '6':
            pdf_qa_system()
        elif choice == '7':
            print("\nThank you for exploring AI examples!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
