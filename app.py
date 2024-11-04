import gradio as gr
import requests
import json

def analyze_stock(ticker: str, 
                 close_price: float, 
                 volume: int, 
                 sma_20: float, 
                 sma_50: float, 
                 rsi: float, 
                 macd: float, 
                 signal_line: float) -> str:
    """
    Analyze stock data using Ollama model and return the prediction
    """
    # Format the stock data
    stock_data = f"""Stock: {ticker}
Close: {close_price:.2f}
Volume: {volume:,}
sou
Technical Indicators:
- SMA (20-day): {sma_20:.2f}
- SMA (50-day): {sma_50:.2f}
- RSI (14-day): {rsi:.2f}
- MACD: {macd:.2f}
- MACD Signal Line: {signal_line:.2f}"""

    # Format the complete prompt
    prompt = f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction: Analyze the provided stock data and provide a trading recommendation with detailed explanations.

### Input: {stock_data}

### Response:"""

    try:
        # Make request to Ollama API with streaming
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': 'stock_adviser',
                'prompt': prompt,
                'stream': True
            },
            stream=True
        )

        # Collect the streamed response
        full_response = ""
        for line in response.iter_lines():
            if line:
                json_response = json.loads(line)
                if 'response' in json_response:
                    full_response += json_response['response']

        return full_response.strip()

    except Exception as e:
        return f"Error generating analysis: {str(e)}"

# Create the Gradio interface
with gr.Blocks(title="Stock Analysis Tool") as demo:
    gr.Markdown("# Stock Analysis Tool")
    gr.Markdown("Enter stock data to get AI-powered analysis and recommendations")
    
    with gr.Row():
        with gr.Column():
            # Input fields
            ticker = gr.Textbox(label="Stock Ticker", placeholder="e.g., AAPL")
            close_price = gr.Number(label="Close Price")
            volume = gr.Number(label="Volume")
            sma_20 = gr.Number(label="20-day SMA")
            sma_50 = gr.Number(label="50-day SMA")
            rsi = gr.Number(label="RSI (14-day)")
            macd = gr.Number(label="MACD")
            signal_line = gr.Number(label="MACD Signal Line")
            
            analyze_btn = gr.Button("Analyze Stock", variant="primary")
        
        with gr.Column():
            # Output area
            output = gr.Textbox(
                label="Analysis Results",
                lines=10,
                placeholder="Analysis will appear here...",
            )
    
    # Example data
    gr.Examples(
        examples=[
            ["AAPL", 175.50, 82345678, 173.25, 170.80, 65.4, 0.75, 0.50],
            ["MSFT", 325.75, 45678901, 320.50, 315.20, 58.7, 1.20, 0.90],
            ["GOOGL", 142.30, 23456789, 140.75, 138.90, 72.3, -0.30, -0.15],
        ],
        inputs=[ticker, close_price, volume, sma_20, sma_50, rsi, macd, signal_line],
        label="Example Stock Data"
    )
    
    # Set up the event handler
    analyze_btn.click(
        fn=analyze_stock,
        inputs=[ticker, close_price, volume, sma_20, sma_50, rsi, macd, signal_line],
        outputs=output
    )

    gr.Markdown("""
    ### How to Use
    1. Enter the stock ticker symbol
    2. Fill in the current price and volume
    3. Add the technical indicators (SMA, RSI, MACD)
    4. Click 'Analyze Stock' to get AI-powered analysis
    
    The tool will provide detailed analysis and trading recommendations based on the provided data.
    """)

# Launch the interface
if __name__ == "__main__":
    demo.launch()  # Added share=True to create a public URL