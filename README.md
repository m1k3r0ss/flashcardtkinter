# Flash Card Application

This is a simple flash card application built using Python and Tkinter, allowing users to practice vocabulary in different languages.

## Features

- Choose from multiple languages including French, Japanese, and German.
- Flip cards to reveal translations.
- Mark words as "weak" to save them for further practice.

## Usage

1. Select a language from the "Language" menu.
2. Click the buttons to navigate through flashcards.
3. Use the "Weak" button to mark words for further practice.

## Adding Custom Word Lists

To add your own word lists in JSON format, follow these steps:

1. Create a new JSON file with your desired language name, e.g., `my_language.json`.
2. Format your JSON file with word-meaning pairs. For example:
   ```json
   {
  "french": [
    {"le": {"romaji": "luh", "english": "the"}},
    {"de": {"romaji": "duh", "english": "of"}},
    {"un": {"romaji": "uhn", "english": "a"}},
    {"à": {"romaji": "ah", "english": "to"}},
]}
   ```
3. Place your JSON file in the `data` directory.
4. Add a new command function in the script to load your custom word list, similar to the existing ones (`sel_japanese`, `sel_french`, etc.).

## Dependencies

- `tkinter`: Python's standard GUI toolkit.
- `tkmacosx` (Optional): Library providing macOS-specific widgets for Tkinter. You can remove this library if you're on Windows, as buttons don't have graphical restrictions on Windows.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
