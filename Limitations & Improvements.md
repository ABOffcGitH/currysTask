## Limitations

- Single PDF Source: Only one ESG document is indexed
- No Ranking or Filtering Logic: Retrieved chunks are similarity-based, not semantic-ranking
- No UI: Currently API-only 
- OpenAI API Dependency: Needs valid OpenAI key and network access.


## Evaluation Strategy

- Context Relevance: Whether retrieved source matches question.
- Latency: End-to-end time from user query to answer.


### Evaluation Methods

- Logging actual vs. expected answers.
- using fixed ESG QA sets.


## Future Improvements

- Add UI 
- Add advanced ranking 


