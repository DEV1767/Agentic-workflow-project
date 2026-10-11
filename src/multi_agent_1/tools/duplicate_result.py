def duplicate_result(results:dict)->list[dict]:
    """
    Remove duplicate research result from multiple search engines.
    Prefer DOI for academic papers,then URL,then title.
    """
    unique_result={}
    final_result=[]

    for source_results in results.values():
        if not isinstance(source_results,list):
            continue

        for item in source_results:
            if not isinstance(item,dict):
                continue

            doi=(item.get("doi")or"").strip().lower()

            url=(item.get("url")or "").strip().lower()

            title="".join(
                (item.get("title")or "").lower().split()
            )

            if doi:
                key=f"doi:{doi}"
            elif url:
                f"url:{url.rstrip('/')}"
            elif title:
                key=f"title:{title}"
            else:
                final_result.append(item)
                continue

            if key not in unique_result:
                unique_result[key]=item
                final_result.append(item)
            else:
                existing = unique_result[key]

                sources = existing.get("sources", [])

                if not sources and existing.get("source"):
                    sources.append(existing["source"])

                new_source = item.get("source")

                if new_source and new_source not in sources:
                    sources.append(new_source)

                existing["sources"] = sources
    
    return final_result