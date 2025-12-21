# Copy your Python files into the container
COPY . /app

# Set the working directory
WORKDIR /app

# (Optional) Create and activate a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install any dependencies (if you have a requirements.txt, uncomment and adjust)
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Run your Python file (change 'guess_num.py' to your main file, e.g., 'guess_2.py')
CMD ["python3", "guess_num.py"]