# AI Story Generator

## Goal

Generate creative stories based on user inputs
**Difficulty**: Beginner

## Implementation

- Gather User inputs interactively
- Gather GROQ API key from an environment variable: GROQ_API_KEY
- Gather Google AI API key from an environment variable: GOOGLE_API_KEY
- Gather genre for the story, such as "fantasy", "sci-fi", "mystery", "adventure", "romance", "thriller", "historical", "mythological"
- Gather audience for the story, such as "children", "teens", "adults"
- Gather plot idea, such as "a bedtime story about funny bunny", "a tech idea by a teenager who became a billionaire even before teens are passed"
- Gather output language, such as "English" (default), "French", "German", "Sanskrit", "Hindi"
- Gather keys to use, such as "All", "GROQ", "Google"
- Gather the length of story in number of pages
- Gather the ending of the story, such as "twist", "cliffhanger", "simple"

### Input Processing

```markup
# Simple text inputs
character = input("Enter a character name: ")
setting = input("Enter a setting: ")
genre = input("Enter a genre (fantasy, sci-fi, mystery): ")
audience = input("Enter an audience (children, teens, adults): ")
plot_idea = input("Enter a plot idea: ")
ouput_language = input("Enter an output language (default is English): ")
keys_to_use = input("Enter keys to use (All, GROQ, Google): ")  
page_length =  input("Enter the length of story in number of pages: ")
story_ending = input("Enter the ending of the story (twist, cliffhanger, simple): ")
```

### Prompt Engineering Strategy

- Use structured prompts with clear instructions
- Include examples of desired output format
- Set creative constraints (word count, style)

```markup
prompt = f"""
Write a {genre} story of {page_length} pages with the following elements:

- Main character: {character}
- Plot : {plot_idea}
- Audience: {audience}
- Output Language: {output_language}

- Include dialogue and descriptive language meant for {audience}.
- Keep the story to the request {genre} and {audience} with an ending matching {story_ending}.
"""
```

### Output Processing

- Clean up formatting
- Add title generation
- Optional: Save stories to file

```markup
# Append the following to the prompt

Come up with an appropriate title for the story. If the story is 2 or more pages, come up with sub-headings as needed.

Ensure the output is nicely formatted in markdown ready for easy print and reading or web-publishing.
```

Save the story into a file with format: `{key_used}_{2-letter-language}_{sanitized-title}.md`, where:

- key_used is either GROQ or GOOLE (not ALL)
- 2-letter-language code (ISO 639 standard) for the selected language - missing this code, using the {language} as default
- sanitized-title is the sanitized title of the story
