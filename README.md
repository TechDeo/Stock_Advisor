# Stock Advisor

## Overview
Stock Advisor is a web application that allows users to input stock data, including technical indicators, and receive AI-powered analysis and trading recommendations. This tool is built using the Gradio library, which provides a user-friendly interface for interacting with the analysis functionality.

## Features
- **User-Friendly Interface**: The tool features a Gradio-based web interface that makes it easy for users to input stock data and view the analysis results.
- **Stock Data Input**: Users can enter the stock ticker, closing price, trading volume, and various technical indicators (SMA, RSI, MACD) to be analyzed.
- **AI-Powered Analysis**: The `analyze_stock()` function formats the input data into a prompt and sends a request to the Ollama API to generate a detailed analysis and trading recommendation.
- **Error Handling**: The tool includes error handling to display meaningful messages to the user if the analysis fails for any reason.
- **Example Data**: The tool provides example stock data that users can leverage to quickly test the analysis functionality.
- **Clear Instructions**: The Gradio interface includes instructions on how to use the Stock Analysis Tool.

## Usage
1. **Enter Stock Data**: Fill in the input fields with the stock ticker, closing price, trading volume, and technical indicators.
2. **Analyze Stock**: Click the "Analyze Stock" button to trigger the analysis.
3. **View Results**: The analysis results, including the trading recommendation, will be displayed in the output area.

## Example
Here's an example of how to use the Stock Analysis Tool:

```python
# Create the Gradio interface
with gr.Blocks(title="Stock Analysis Tool") as demo:
    # Input fields and button
    ticker = gr.Textbox(label="Stock Ticker", placeholder="e.g., AAPL")
    close_price = gr.Number(label="Close Price")
    volume = gr.Number(label="Volume")
    sma_20 = gr.Number(label="20-day SMA")
    sma_50 = gr.Number(label="50-day SMA")
    rsi = gr.Number(label="RSI (14-day)")
    macd = gr.Number(label="MACD")
    signal_line = gr.Number(label="MACD Signal Line")
    analyze_btn = gr.Button("Analyze Stock", variant="primary")

    # Output area
    output = gr.Textbox(
        label="Analysis Results",
        lines=10,
        placeholder="Analysis will appear here...",
    )

    # Set up the event handler
    analyze_btn.click(
        fn=analyze_stock,
        inputs=[ticker, close_price, volume, sma_20, sma_50, rsi, macd, signal_line],
        outputs=output
    )

# Launch the interface
if __name__ == "__main__":
    demo.launch()
```

## Installation
To use the Stock Analysis Tool, you'll need to have the following dependencies installed:

- `gradio`
- `requests`
- `json`

You can install these dependencies using pip:

```
pip install gradio requests
```

## Contributing
We welcome contributions to the Stock Analysis Tool project. If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Push your branch to your forked repository
5. Submit a pull request to the main repository

## License
This project is licensed under the [MIT License](LICENSE).