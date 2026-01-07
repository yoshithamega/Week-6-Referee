def compare_services(budget, scalability, management):
    result = []

    if budget == "low":
        result.append("Lambda is cost-effective for low budget use cases.")
        result.append("EC2 may incur higher costs if not monitored.")

    if scalability == "high":
        result.append("Lambda and ECS scale automatically.")
        result.append("EC2 requires manual scaling.")

    if management == "minimal":
        result.append("Lambda needs no server management.")
        result.append("ECS reduces infrastructure burden.")

    if management == "full":
        result.append("EC2 gives full control over servers.")

    return result
