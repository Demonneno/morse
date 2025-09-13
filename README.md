# <subfolder> Morse code

## Overview
This project contains the `<Morse>` module, a Python application/library for encoding and decoding Morse. It was originally part of a larger private repository and is now shared publicly.

## Installation

### Prerequisites
- Python 3.8 or higher
- Astral uv

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/user/public-subfolder-repo.git
   cd subfolder-repo
   ```

## Usage
To run the main script (e.g., `main.py`):
```bash
python main.py
```

For example usage:
```python
# Example code snippet
 print_codes(encode_list)
 message = input('\nEnter your message: ').upper()

 allowed = ['.', '-', '/', ' ']
 print_codes(decode_list)
 message = input('\nEnter your code with forward slash separators between words (.- .- / .- .-): ')
```

## Dependencies
Current version of `<Morse>` does not have any dependencies.

Optional for testing: `pytest`.

See `pyproject.toml` for the full list of dependencies.

## Running Tests
This is optional and requires updating `uv`. See 'Dependencies' for more information.
To run tests with `pytest`:
```bash
uv run pytest
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions, contact Neno at <demonneno1@gmail.com> or open an issue on GitHub.
