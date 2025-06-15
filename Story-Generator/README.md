# Story Generator

> Interactive story generation using AI with customizable parameters

## Quick Start

```bash
# Run the story generator
python main.py
```

Follow the interactive prompts to create your story!

## What This Project Does

Generate creative stories by gathering user preferences through an interactive command-line interface:

- 📝 **Character & Setting**: Define your protagonist and story world
- 🎭 **Genre Selection**: Choose from 8 different story genres  
- 👥 **Audience Targeting**: Stories tailored for children, teens, or adults
- 🌍 **Language Output**: Generate stories in multiple languages
- 📏 **Length Control**: Set minimum and maximum character limits
- 🎬 **Ending Styles**: Choose how your story concludes

## Story Customization Options

| Setting | Available Options |
|---------|-------------------|
| **Genres** | Fantasy, Sci-fi, Mystery, Adventure, Romance, Thriller, Historical, Mythological |
| **Audiences** | Children, Teens, Adults |
| **Ending Styles** | Twist, Cliffhanger, Simple |
| **Languages** | English, French, German, Hindi, Sanskrit, Spanish, and more |
| **Story Length** | 200-20,000 characters (customizable range) |

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
| **Character Name** | Any name | "Robinhood", "Luna" |
| **Plot Setting** | Any setting | "Ocean rescue", "Space station" |
| **Genre** | `fantasy`, `sci-fi`, `mystery`, `adventure`, `romance`, `thriller`, `historical`, `mythological` | `fantasy` |
| **Audience** | `children`, `teens`, `adults` | `children` |
| **Language** | Any language name | "English", "French", "German" |
| **API Provider** | `All`, `GROQ`, `GEMINI`, `OPENAI` | `All` |
| **Story Length** | Min-Max characters | 200-2000 |
| **Ending Style** | `twist`, `cliffhanger`, `simple` | `simple` |

### Example Session

```
Enter a character name: Luna
Enter a plot setting for your story: Magic forest adventure
Enter a genre ['fantasy', 'sci-fi', 'mystery', ...]: fantasy
Enter an audience ['children', 'teens', 'adults']: children
Enter an output language: English
Enter key to use ['All', 'GROQ', 'GEMINI', 'OPENAI']: GROQ
Enter the minimum character limit (default 200): 500
Enter the maximum character limit (default 20000): 1500
Enter the ending of the story ['twist', 'cliffhanger', 'simple']: simple
```

## Output

Stories are automatically saved as:

```
{PROVIDER}_{LANGUAGE_CODE}_{SANITIZED_TITLE}.txt
```

**Examples:**

- `GROQ_en_Lunas_Magic_Adventure.txt`
- `GEMINI_fr_Le_Voyage_Mysterieux.txt`
- `OPENAI_de_Das_Grosse_Abenteuer.txt`

## Supported Languages

The system supports any language name and automatically converts to ISO 639-1 codes:

| Language | Code | Language | Code |
|----------|------|----------|------|
| English | en | French | fr |
| German | de | Hindi | hi |
| Sanskrit | sa | Spanish | es |

## Error Handling

- **Robust JSON parsing** with fallback methods
- **Graceful API failures** - continues with other providers
- **Input validation** for all user inputs
- **Automatic retry** for network issues

## File Structure

```
Story-Generator/
├── main.py              # Main application
├── README.md            # This file
├── config.py            # Configuration (if added)
└── examples/            # Example outputs (if added)
```

## Development

For implementation details, prompt engineering strategies, and technical documentation, see:

- 📋 **[Implementation Guide](IMPLEMENTATION.md)** - Code structure and prompt engineering
- 🏗️ **[Framework Documentation](../README.md)** - Multi-provider AI library details
- 🛠️ **[Development Setup](../docs/)** - General development guidelines

### Project Structure

```
Story-Generator/
├── main.py              # Interactive story generation interface
├── README.md            # User guide (this file)
├── IMPLEMENTATION.md    # Technical implementation details
└── examples/            # Sample generated stories
```

## Troubleshooting

### Common Issues

**Import Error**: Make sure you installed the package from parent directory:

```bash
cd .. && pip install -e .
```

**API Key Error**: Check your `.env` file has the correct API keys set.

**JSON Parse Error**: The system has fallback parsing - check the generated file for content even if you see parsing warnings.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with different providers and languages
5. Submit a pull request

## License

MIT License - feel free to use in your projects!
