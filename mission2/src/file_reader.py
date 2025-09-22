class FileReader:
    @staticmethod
    def parse_file(file_path):
        args = []
        with open(file_path, encoding='utf-8', mode='r') as f:
            for _ in range(500):
                line = f.readline()
                parts = line.strip().split()
                assert len(parts) == 2
                args.append((parts[0], parts[1]))
        return args   