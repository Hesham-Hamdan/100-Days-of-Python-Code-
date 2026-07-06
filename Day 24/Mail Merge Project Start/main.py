# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Day 24\Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
    starting_letter = file.read()
with open(
    "Day 24\Mail Merge Project Start\Input\Invited_Names\invited_names.txt"
) as file:
    names = file.readlines()

for name in names:
    stripped_name = name.strip("\n")
    final_letter = starting_letter.replace("[name]", stripped_name)
    with open(
        f"Day 24\Mail Merge Project Start\Output\ReadyToSend\{stripped_name}.txt",
        mode="w",
    ) as invite:
        invite.write(final_letter)
