def output_links(obj):
    links = []
    for gif in obj['data']:
        links.append(gif['url'])
    return links
