class BaseClass:

    def load_textfile(text_file_path):
        with open(text_file_path) as file:
            event_details = []
            for line in file:
                event_details.append(line.strip())
        return(event_details)

    def inner_text_tolist(in_text):
        lines = (line.strip() for line in in_text.splitlines())
        event_details_test = [line for line in lines if line != ""]
        return(event_details_test)