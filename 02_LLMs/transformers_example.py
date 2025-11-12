"""
Transformers Example
Demonstrates using Hugging Face transformers library for text generation.
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import warnings

warnings.filterwarnings('ignore')

def check_device():
    """Check if CUDA is available"""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"💻 Using device: {device}")
    if device == "cpu":
        print("   ℹ️  Running on CPU (slower but works everywhere)")
    return device

def simple_text_generation():
    """Basic text generation with a small model"""
    print("\n" + "=" * 60)
    print("1. SIMPLE TEXT GENERATION")
    print("=" * 60)
    
    try:
        # Use a small, efficient model
        model_name = "gpt2"
        print(f"\n📦 Loading model: {model_name}")
        print("   (First run will download ~500MB)")
        
        # Create text generation pipeline
        generator = pipeline(
            "text-generation",
            model=model_name,
            device=-1  # CPU
        )
        
        prompt = "Artificial intelligence is"
        print(f"\n📝 Prompt: '{prompt}'")
        
        # Generate text
        outputs = generator(
            prompt,
            max_length=50,
            num_return_sequences=2,
            temperature=0.8,
            do_sample=True
        )
        
        print("\n🤖 Generated texts:")
        for i, output in enumerate(outputs, 1):
            print(f"\n   {i}. {output['generated_text']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Note: This requires internet for first-time model download")

def tokenization_example():
    """Show how tokenization works"""
    print("\n" + "=" * 60)
    print("2. TOKENIZATION")
    print("=" * 60)
    
    try:
        tokenizer = AutoTokenizer.from_pretrained("gpt2")
        
        text = "AI-Essentials: Learn artificial intelligence!"
        print(f"\n📝 Input text: '{text}'")
        
        # Tokenize
        tokens = tokenizer.tokenize(text)
        print(f"\n🔤 Tokens: {tokens}")
        print(f"📊 Number of tokens: {len(tokens)}")
        
        # Convert to IDs
        token_ids = tokenizer.encode(text)
        print(f"\n🔢 Token IDs: {token_ids}")
        
        # Decode back
        decoded = tokenizer.decode(token_ids)
        print(f"\n📤 Decoded: '{decoded}'")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def model_comparison():
    """Compare different model sizes"""
    print("\n" + "=" * 60)
    print("3. MODEL COMPARISON")
    print("=" * 60)
    
    models_info = [
        ("gpt2", "124M parameters", "Fast, good for simple tasks"),
        ("gpt2-medium", "355M parameters", "Better quality, slower"),
        ("gpt2-large", "774M parameters", "High quality, much slower"),
        ("distilgpt2", "82M parameters", "Distilled version, very fast"),
    ]
    
    print("\n📊 Available GPT-2 variants:\n")
    for name, params, desc in models_info:
        print(f"   • {name:15} - {params:20} - {desc}")
    
    print("\n💡 Recommendation: Start with 'gpt2' or 'distilgpt2'")

def controlled_generation():
    """Demonstrate controlled text generation"""
    print("\n" + "=" * 60)
    print("4. CONTROLLED GENERATION")
    print("=" * 60)
    
    try:
        generator = pipeline("text-generation", model="gpt2", device=-1)
        
        prompt = "The future of machine learning is"
        print(f"\n📝 Prompt: '{prompt}'")
        
        # Different temperature settings
        temperatures = [0.3, 0.7, 1.2]
        
        for temp in temperatures:
            print(f"\n🌡️  Temperature: {temp}")
            output = generator(
                prompt,
                max_length=30,
                temperature=temp,
                do_sample=True,
                num_return_sequences=1
            )[0]['generated_text']
            
            print(f"   {output}")
        
        print("\n💡 Lower temperature = more deterministic")
        print("   Higher temperature = more creative/random")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("TRANSFORMERS LIBRARY EXAMPLES")
    print("=" * 60)
    
    device = check_device()
    
    print("\nℹ️  These examples use Hugging Face transformers")
    print("   Models will be downloaded on first run (~500MB)")
    print("   Subsequent runs will use cached models")
    
    # Run examples
    simple_text_generation()
    tokenization_example()
    model_comparison()
    controlled_generation()
    
    print("\n" + "=" * 60)
    print("✅ All examples completed!")
    print("=" * 60)
    print("\n💡 Key Takeaways:")
    print("   1. Transformers enable easy access to pre-trained models")
    print("   2. Tokenization breaks text into model-digestible pieces")
    print("   3. Temperature controls generation randomness")
    print("   4. Different model sizes trade speed for quality")
    print("\n🔗 Next steps:")
    print("   - Explore Hugging Face Hub for more models")
    print("   - Try fine-tuning models on your data")
    print("   - Learn about prompt engineering")
    print("\n")

if __name__ == "__main__":
    main()
