import markovify


def generate_model(filename, size=2):
    """Model generator from text."""

    # We read whole document:
    with open(filename) as f:
        text = f.read()

    # Build and return model:
    text_model = markovify.Text(text, state_size=size)

    return text_model
