import Analyzer

analyzer = Analyzer.Analyzer()
analyzer.get_from_file("1.txt")
analyzer.analyze()
analyzer.save()
analyzer.show()
