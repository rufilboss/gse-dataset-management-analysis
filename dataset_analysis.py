"""
Dataset Management and Basic Analysis System

This program reads numerical data from a CSV file, performs statistical analysis,
and extracts unique categories from a categorical data file.
"""


class DataSet:
    """
    A class to manage and analyze datasets.
    
    This class handles loading numerical data, calculating statistics,
    and displaying results.
    """
    
    def __init__(self, data_file, categorical_file, threshold=85):
        """
        Initialize the DataSet object.
        
        Args:
            data_file (str): Path to the numerical data CSV file
            categorical_file (str): Path to the categorical data CSV file
            threshold (float): Threshold value for performance evaluation (default: 85)
        """
        self.data_file = data_file
        self.categorical_file = categorical_file
        self.threshold = threshold
        self.data = []
        self.categories = set()
        self.statistics = {}
    
    def load_data(self):
        """
        Load numerical data from CSV file.
        
        Handles errors for missing files, empty files, and invalid data.
        """
        try:
            # Try to open and read the file
            with open(self.data_file, 'r') as file:
                lines = file.readlines()
            
            # Check if file is empty
            if not lines:
                raise ValueError("File is empty")
            
            # Read and convert each line to a number
            for line in lines:
                line = line.strip()  # Remove whitespace
                if line:  # Skip empty lines
                    try:
                        # Convert to float to handle decimal numbers
                        value = float(line)
                        self.data.append(value)
                    except ValueError:
                        # Handle invalid (non-numeric) values
                        raise ValueError(f"Invalid data found: '{line}' is not a number")
            
            # Check if we have any valid data
            if not self.data:
                raise ValueError("No valid numerical data found in file")
            
            print(f"Successfully loaded {len(self.data)} data points")
            
        except FileNotFoundError:
            print(f"Error: File '{self.data_file}' not found")
            raise
        except ValueError as e:
            print(f"Error: {e}")
            raise
    
    def calculate_total(self, dataset):
        """
        Calculate the total sum of all values in the dataset.
        
        Args:
            dataset (list): List of numerical values
            
        Returns:
            float: Total sum of all values
        """
        total = 0
        # Use loop to add each value
        for value in dataset:
            total = total + value  # Using + operator
        return total
    
    def calculate_average(self, dataset):
        """
        Calculate the average of all values in the dataset.
        
        Args:
            dataset (list): List of numerical values
            
        Returns:
            float: Average value
        """
        if not dataset:
            return 0
        
        # Count the number of data points
        count = 0
        for value in dataset:
            count = count + 1  # Count using loop
        
        # Calculate total using the function
        total = self.calculate_total(dataset)
        
        # Calculate average using / operator
        average = total / count
        return average
    
    def calculate_minimum(self, dataset):
        """
        Find the minimum value in the dataset.
        
        Args:
            dataset (list): List of numerical values
            
        Returns:
            float: Minimum value
        """
        if not dataset:
            return None
        
        # Initialize with first value
        minimum = dataset[0]
        
        # Use loop to compare each value
        for value in dataset:
            if value < minimum:  # Using comparison operator
                minimum = value
        
        return minimum
    
    def calculate_maximum(self, dataset):
        """
        Find the maximum value in the dataset.
        
        Args:
            dataset (list): List of numerical values
            
        Returns:
            float: Maximum value
        """
        if not dataset:
            return None
        
        # Initialize with first value
        maximum = dataset[0]
        
        # Use loop to compare each value
        for value in dataset:
            if value > maximum:  # Using comparison operator
                maximum = value
        
        return maximum
    
    def calculate_statistics(self):
        """
        Calculate all statistics for the loaded dataset.
        
        Stores results in self.statistics dictionary.
        """
        if not self.data:
            print("No data loaded. Please load data first.")
            return
        
        # Calculate all statistics
        self.statistics['total'] = self.calculate_total(self.data)
        self.statistics['average'] = self.calculate_average(self.data)
        self.statistics['minimum'] = self.calculate_minimum(self.data)
        self.statistics['maximum'] = self.calculate_maximum(self.data)
        self.statistics['count'] = len(self.data)
    
    def load_categories(self):
        """
        Load categorical data and extract unique values using a set.
        """
        try:
            # Try to open and read the categorical file
            with open(self.categorical_file, 'r') as file:
                lines = file.readlines()
            
            # Check if file is empty
            if not lines:
                raise ValueError("Categorical file is empty")
            
            # Extract unique values using a set
            for line in lines:
                line = line.strip()  # Remove whitespace
                if line:  # Skip empty lines
                    self.categories.add(line)  # Set automatically handles uniqueness
            
            if not self.categories:
                raise ValueError("No valid categories found in file")
            
            print(f"Successfully loaded {len(self.categories)} unique categories")
            
        except FileNotFoundError:
            print(f"Error: File '{self.categorical_file}' not found")
            raise
        except ValueError as e:
            print(f"Error: {e}")
            raise
    
    def display_results(self):
        """
        Display the calculated statistics and performance evaluation.
        
        Uses conditional statements to evaluate performance based on average.
        """
        if not self.statistics:
            print("No statistics calculated. Please calculate statistics first.")
            return
        
        print("\n" + "="*50)
        print("DATASET ANALYSIS RESULTS")
        print("="*50)
        print(f"Total data points: {self.statistics['count']}")
        print(f"Total: {self.statistics['total']}")
        print(f"Average: {self.statistics['average']:.2f}")
        print(f"Minimum: {self.statistics['minimum']}")
        print(f"Maximum: {self.statistics['maximum']}")
        
        # Conditional statement for performance evaluation
        if self.statistics['average'] > self.threshold:
            print(f"\nPerformance: High Performance")
            print(f"(Average {self.statistics['average']:.2f} is above threshold {self.threshold})")
        else:
            print(f"\nPerformance: Needs Improvement")
            print(f"(Average {self.statistics['average']:.2f} is below threshold {self.threshold})")
        
        # Display unique categories
        print("\n" + "-"*50)
        print("CATEGORICAL DATA ANALYSIS")
        print("-"*50)
        print(f"Total unique categories: {len(self.categories)}")
        print("Unique categories:", sorted(self.categories))
        print("="*50 + "\n")
    
    def save_results(self, output_file='analysis_report.txt'):
        """
        Save the computed statistics and unique category count to a report file.
        
        Args:
            output_file (str): Path to the output report file
        """
        try:
            with open(output_file, 'w') as file:
                file.write("="*50 + "\n")
                file.write("DATASET ANALYSIS REPORT\n")
                file.write("="*50 + "\n\n")
                
                file.write("NUMERICAL DATA STATISTICS\n")
                file.write("-"*50 + "\n")
                file.write(f"Data file: {self.data_file}\n")
                file.write(f"Total data points: {self.statistics['count']}\n")
                file.write(f"Total: {self.statistics['total']}\n")
                file.write(f"Average: {self.statistics['average']:.2f}\n")
                file.write(f"Minimum: {self.statistics['minimum']}\n")
                file.write(f"Maximum: {self.statistics['maximum']}\n\n")
                
                # Performance evaluation
                if self.statistics['average'] > self.threshold:
                    file.write(f"Performance: High Performance\n")
                    file.write(f"(Average {self.statistics['average']:.2f} is above threshold {self.threshold})\n\n")
                else:
                    file.write(f"Performance: Needs Improvement\n")
                    file.write(f"(Average {self.statistics['average']:.2f} is below threshold {self.threshold})\n\n")
                
                file.write("CATEGORICAL DATA ANALYSIS\n")
                file.write("-"*50 + "\n")
                file.write(f"Categories file: {self.categorical_file}\n")
                file.write(f"Total unique categories: {len(self.categories)}\n")
                file.write(f"Unique categories: {', '.join(sorted(self.categories))}\n")
                file.write("="*50 + "\n")
            
            print(f"Results saved to '{output_file}'")
            
        except Exception as e:
            print(f"Error saving results: {e}")


def main():
    """
    Main function to run the dataset analysis.
    """
    # Create DataSet object
    dataset = DataSet(
        data_file='student_marks.csv',
        categorical_file='courses.csv',
        threshold=85
    )
    
    # Load numerical data
    try:
        dataset.load_data()
    except (FileNotFoundError, ValueError):
        return
    
    # Calculate statistics
    dataset.calculate_statistics()
    
    # Load categorical data
    try:
        dataset.load_categories()
    except (FileNotFoundError, ValueError):
        pass  # Continue even if categorical file fails
    
    # Display results
    dataset.display_results()
    
    # Save results to file
    dataset.save_results('analysis_report.txt')


if __name__ == "__main__":
    main()

