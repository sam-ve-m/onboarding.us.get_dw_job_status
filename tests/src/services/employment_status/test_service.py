from src.domain.enums.drive_wealth.employment_status import EmploymentStatus
from src.services.employment_status.service import EmploymentStatusService
import pytest


@pytest.mark.asyncio
async def test_get_employment_status_enum():
    result = await EmploymentStatusService.get_employment_status_enum()
    expected_result = [
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
    assert result == expected_result
