# Bionic Text Processor

This Python script processes a text file and uses artificial fixation to bold a fraction of words based on their length. I was inspired to create this project due to my own difficulty in reading quickly. As someone with ADHD, reading in this format helps me read quickly and comprehend what I am reading. Therefore, I decided to develop this project to assist others who are unable to afford the high cost associated with accessing similar applications.

## Installation

1. No additional instalations required for this app, as long as you are running Python 3

2. Save the code as `bionic.py`.

## Usage

1. Place the `bold_text_processor.py` script and the input text file, `input.txt`, in the same directory.

2. Open a terminal window and navigate to the directory containing the script and input file.

3. Run the script using the following command:
```bash
python bionic.py
```

## Input File

The input file, `input.txt`, should contain plain text. Each word of text will be processed independently.

## Output File

The processed text will be saved to a new file named `output.txt`.

## Algorithm

The script iterates through each line of the input text, splitting it into a list of words. For each word, the script checks its length and applies bold formatting accordingly:

* Words with one or no characters are left unchanged.
* Words with two to three characters receive bold formatting on the first character.
* Words with four to five characters receive bold formatting on the first two characters.
* Words with six characters receive bold formatting on the first three characters.
* Words with seven or more characters receive bold formatting on the first four characters.

Finally, the processed line of text is written to the output file.

## Example

If the input file, `input.txt`, contains the following text:

```
This is an example text file.
It contains sentences of varying lengths.
Some words are short, while others are long.
```

The output file, `output.txt`, will contain the following text:

```
**Th**is **i**s **a**n **exam**ple **te**xt **fi**le.
**I**t **cont**ains **sent**ences **o**f **vary**ing **leng**ths.
**So**me **wo**rds **a**re **sh**ort, **wh**ile **oth**ers **a**re **lo**ng.
```
## Then a copy and paste to any markdown processor, e.g Notion and the result will be as follows:


**Th**is **i**s **a**n **exam**ple **te**xt **fi**le.

**I**t **cont**ains **sent**ences **o**f **vary**ing **leng**ths.

**So**me **wo**rds **a**re **sh**ort, **wh**ile **oth**ers **a**re **lo**ng.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributions

Welcome! Feel free to contribute to this project by submitting pull requests or reporting issues.
