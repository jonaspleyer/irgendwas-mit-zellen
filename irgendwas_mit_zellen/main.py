import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e",
        "--embedding",
        default=None,
        help="The embedding to use for following calculations",
    )
    pyargs = parser.parse_args()

    if pyargs.embedding is not None:
        print(pyargs.embedding)
    else:
        print("Generating new embedding")
