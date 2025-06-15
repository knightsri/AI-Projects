# {PROJECT_NAME}

> {PROJECT_DESCRIPTION}

## Quick Start

```bash
# Run the {PROJECT_NAME_LOWERCASE}
python main.py
```

{USAGE_DESCRIPTION}

## What This Project Does

{DETAILED_PROJECT_DESCRIPTION}

Key features:

- {FEATURE_1}
- {FEATURE_2}
- {FEATURE_3}
- {FEATURE_4}

## {MAIN_CONFIGURATION_SECTION}

| Setting | Available Options |
|---------|-------------------|
| **{CONFIG_1_NAME}** | {CONFIG_1_OPTIONS} |
| **{CONFIG_2_NAME}** | {CONFIG_2_OPTIONS} |
| **{CONFIG_3_NAME}** | {CONFIG_3_OPTIONS} |
| **{CONFIG_4_NAME}** | {CONFIG_4_OPTIONS} |

## Prerequisites

This project uses the shared `gai_lib` framework. See the [main project setup](../README.md) for:

- API key configuration
- Framework installation  
- Dependency management

## Usage

### Interactive Mode

```bash
python main.py
```

You'll be prompted for:

| Input | Options | Example |
|-------|---------|---------|
| **{INPUT_1_NAME}** | {INPUT_1_OPTIONS} | {INPUT_1_EXAMPLE} |
| **{INPUT_2_NAME}** | {INPUT_2_OPTIONS} | {INPUT_2_EXAMPLE} |
| **{INPUT_3_NAME}** | {INPUT_3_OPTIONS} | {INPUT_3_EXAMPLE} |
| **{INPUT_4_NAME}** | {INPUT_4_OPTIONS} | {INPUT_4_EXAMPLE} |

### Example Session

```
{EXAMPLE_INPUT_1}: {EXAMPLE_VALUE_1}
{EXAMPLE_INPUT_2}: {EXAMPLE_VALUE_2}
{EXAMPLE_INPUT_3}: {EXAMPLE_VALUE_3}
{EXAMPLE_INPUT_4}: {EXAMPLE_VALUE_4}
```

## Output

{OUTPUT_DESCRIPTION}

**Examples:**

- `{OUTPUT_EXAMPLE_1}`
- `{OUTPUT_EXAMPLE_2}`
- `{OUTPUT_EXAMPLE_3}`

## {SPECIALIZED_SECTION_TITLE}

{SPECIALIZED_SECTION_CONTENT}

## Error Handling

- **Robust JSON parsing** with fallback methods
- **Graceful API failures** - continues with other providers
- **Input validation** for all user inputs
- **Automatic retry** for network issues

## File Structure

```
{PROJECT_NAME}/
├── main.py              # {MAIN_PY_DESCRIPTION}
├── README.md            # This file
├── IMPLEMENTATION.md    # Technical implementation details
└── examples/            # {EXAMPLES_DESCRIPTION}
```

## Development

For implementation details, prompt engineering strategies, and technical documentation, see:

- 📋 **[Implementation Guide](IMPLEMENTATION.md)** - Code structure and prompt engineering
- 🏗️ **[Framework Documentation](../README.md)** - Multi-provider AI library details
- 🛠️ **[Development Setup](../docs/)** - General development guidelines

### Project Structure

```
{PROJECT_NAME}/
├── main.py              # {MAIN_PY_DESCRIPTION}
├── README.md            # User guide (this file)
├── IMPLEMENTATION.md    # Technical implementation details
└── examples/            # {EXAMPLES_DESCRIPTION}
```

## Troubleshooting

### Common Issues

**Import Error**: Make sure you installed the package from parent directory:

```bash
cd .. && pip install -e .
```

**API Key Error**: Check your `.env` file has the correct API keys set.

**JSON Parse Error**: The system has fallback parsing - check the generated file for content even if you see parsing warnings.

{PROJECT_SPECIFIC_TROUBLESHOOTING}

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with different providers and {PROJECT_SPECIFIC_TESTING}
5. Submit a pull request

## License

MIT License - feel free to use in your projects!
