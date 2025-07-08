def get_analysis_prompt(clause):
    prompt_template = """
    Analyze the following contract clause:
    {clause}

    For this clause, provide:
    1. **Observation**: Summarize the main point or concern in this clause.
    2. **Compliance Risks**: Highlight compliance or regulatory risks (S166, restructuring, etc.)
    3. **Recommendation**: Suggest improvements or actions to address any issues found.
    """
    return prompt_template.format(clause=clause)