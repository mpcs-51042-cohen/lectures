class FileProcessor:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.processed_lines = 0
    
    def read_file(self):
        with open(self.input_path, 'r') as f:
            return f.readlines()
    
    def process_line(self, line):
        # Base implementation just returns the line unchanged
        return line
    
    def process(self):
        lines = self.read_file()
        with open(self.output_path, 'w') as out:
            for line in lines:
                processed = self.process_line(line)
                out.write(processed)
                self.processed_lines += 1
        print(f"Processed {self.processed_lines} lines")


class CSVCleaner(FileProcessor):
    def __init__(self, input_path, output_path, delimiter=','):
        super().__init__(input_path, output_path)
        self.delimiter = delimiter
        self.removed_empty = 0
    
    def process_line(self, line):
        # Remove lines with empty fields
        fields = line.strip().split(self.delimiter)
        if any(field == '' for field in fields):
            self.removed_empty += 1
            return ''  # Skip this line
        return line
    
    def process(self):
        super().process()
        print(f"Removed {self.removed_empty} rows with empty fields")


class LogRedactor(FileProcessor):
    def __init__(self, input_path, output_path, sensitive_terms):
        super().__init__(input_path, output_path)
        self.sensitive_terms = sensitive_terms
        self.redactions = 0
    
    def process_line(self, line):
        # Redact sensitive information
        redacted = line
        for term in self.sensitive_terms:
            if term in redacted:
                redacted = redacted.replace(term, '[REDACTED]')
                self.redactions += 1
        return redacted
    
    def process(self):
        super().process()
        print(f"Made {self.redactions} redactions")


csv_cleaner = CSVCleaner('raw_data.csv', 'clean_data.csv')
csv_cleaner.process()

log_redactor = LogRedactor(
    'app.log', 
    'sanitized.log',
    sensitive_terms=['password=', 'api_key=', 'ssn:']
)
log_redactor.process()