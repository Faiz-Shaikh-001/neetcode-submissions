class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def resolveLocal(localName: str) -> str:
            # if includes '+' then keep only lhs
            # replace '.' with ''

            localName = localName.split('+')[0]
            localName = localName.replace('.', '')

            return localName


        uniqueEmails = defaultdict(set)
        for email in emails:
            seperatedEmail = email.split('@')  
            if len(seperatedEmail) != 2:
                continue
            
            localName, domainName = seperatedEmail
            resolvedLocalName = resolveLocal(localName)
            uniqueEmails[domainName].add(resolvedLocalName)
        
        result = 0
        for domain in uniqueEmails:
            result += len(uniqueEmails[domain])
        
        return result

    

