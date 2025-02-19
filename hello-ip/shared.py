from dataclasses import dataclass


@dataclass
class WorkflowInput:
    name: str
    seconds: int = 0


@dataclass
class WorkflowOutput:
    ip_addr: str
    location: str


DEMO_OPTIONS = """
    <div class="mt-2 p-2 bg-gray-50 rounded-md">
        <label for="sleep_duration" class="block text-sm font-medium text-gray-700">
            Sleep Duration (seconds)
        </label>
        <input 
            type="number" 
            name="sleep_duration" 
            id="sleep_duration"
            min="0" 
            max="10" 
            step="1"
            placeholder="Number of seconds" 
            class="mt-1 w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-brand-primary focus:border-brand-primary"
        >
    </div>
    """
