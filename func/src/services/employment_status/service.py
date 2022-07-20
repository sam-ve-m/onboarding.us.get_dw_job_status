from typing import List

from src.domain.enums.drive_wealth.employment_status import EmploymentStatus


class EmploymentStatusService:
    @classmethod
    async def get_employment_status_enum(cls) -> List[dict]:
        employment_status = [
            {"code": EmploymentStatus.EMPLOYED.value, "value": "EMPREGADO(A)"},
            {"code": EmploymentStatus.RETIRED.value, "value": "APOSENTADO(A)"},
            {"code": EmploymentStatus.STUDENT.value, "value": "ALUNO(A)"},
            {
                "code": EmploymentStatus.UNEMPLOYED.value,
                "value": "DESEMPREGADO(A)",
            },
            {
                "code": EmploymentStatus.SELF_EMPLOYED.value,
                "value": "TRABALHADOR(A) POR CONTA PRÓPRIA",
            },
        ]

        return employment_status
