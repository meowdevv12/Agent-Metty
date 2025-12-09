# Metty Quick Start Guide

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/metty-defi-analytics.git
cd metty-defi-analytics
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure API keys:
```bash
cp config.example.py config.py
# Edit config.py with your API keys
```

## Usage
```bash
python src/main.py --pool 0x1234... --chain ethereum
```

## Next Steps

- Read [architecture.md](architecture.md) for system design
- Check [api_reference.md](api_reference.md) for API documentation
